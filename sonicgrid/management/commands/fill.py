from types import NoneType

from django.core.management import BaseCommand
from sonicgrid.models import Publisher, Copyrighter, Rightholder, Genre

import os
import random
import json
from bs4 import BeautifulSoup
from pathlib import Path
from django.conf import settings

destination_directory = "{}/sonicgrid/db/".format(settings.BASE_DIR)


def parse(library_id):
    current_directory_name = f"{destination_directory}{library_id}"
    file_path = f'{current_directory_name}/{library_id}.html'

    # parse 'html'

    try:
        with open(file_path, 'r', encoding='utf-8') as fp:
            html_content = fp.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        # extract info
        dom_script_json = soup.find('script', attrs={'id': '__NEXT_DATA__', 'type': 'application/json'})
        dom_script = json.loads(dom_script_json.text)
        dom_initial_state = dom_script["props"]["pageProps"]["initialState"]
        initial_state = json.loads(dom_initial_state)
        # key = f'getArtFiles({{"artId":{library_id}}})'
        # files = initial_state['rtkqApi']['queries'][key]['data']

        key = f'getArtData({{"artIdOrSlug":{library_id}}})'
        bookdata = initial_state['rtkqApi']['queries'][key]['data']
        return bookdata

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def getdata(library_id):
    Dirs = os.popen(f'find {destination_directory} -mindepth 1 -maxdepth 1 -type d').read().split()
    for Dir in Dirs:
        library_id = Dir.split('/')[-1]
        data = parse(library_id)



class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        запуск отдельной функции
        """
        self.clear_databases()
        self.handle_bulk_create(*args, **options)
        print("Success!!!")

    def clear_databases(self):
        Publisher.objects.all().delete()
        Genre.objects.all().delete()
        Copyrighter.objects.all().delete()
        Rightholder.objects.all().delete()

    def handle_bulk_create_publisher(self, *args, **options):
        """
        заполнение с одним обращением в базу данных с
        записью множества строк одновременно
        """
        object_list = [
            {'id': 85198, 'name': 'Фантом Пресс', 'url': 'publisher/fantom-press/'}
        ]
        objects_for_creation = []
        for object_item in object_list:
            objects_for_creation.append(Publisher(**object_item))
        Publisher.objects.bulk_create(objects_for_creation)

    def handle_bulk_create(self, *args, **options):
        """
        заполнение с одним обращением в базу данных с
        записью множества строк одновременно
        """
        Dirs = os.popen(f'find {destination_directory} -mindepth 1 -maxdepth 1 -type d').read().split()
        for Dir in Dirs:
            library_id = Dir.split('/')[-1]
            library_data = parse(library_id)
            print(library_id)
            if library_data is not NoneType and library_data is not None:
                publisher = None
                copyrighter = None
                rightholder = None

                if library_data["publisher"] is not None:
                    if library_data["publisher"]["id"] is not None:
                        publisher, created = Publisher.objects.get_or_create( ** library_data["publisher"] )
                if library_data["copyrighter"]["id"] is not None:
                    copyrighter, created = Copyrighter.objects.get_or_create( ** library_data["copyrighter"] )
                if len(library_data["rightholders"])>0:
                    for rightholder in library_data["rightholders"]:
                        if rightholder["id"] is not None:
                            Rightholder.objects.get_or_create( ** rightholder )
                if len(library_data["genres"])>0:
                    for genre in library_data["genres"]:
                        print(genre)
                        if genre["id"] is not None:
                            genre['is_root']=False
                            genre['is_main']=True
                            Genre.objects.get_or_create( ** genre )

