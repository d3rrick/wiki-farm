
import click
import os
@click.command()
@click.option('--dbname', help="Database name",prompt=True)
@click.option('--shapefile',help='name of shapefile',prompt=True)

def ogr2ogr(dbname,shapefile):
	os.system('ogr2ogr -append -f "PostgreSQL" PG:"dbname={}" {}'.format(dbname,shapefile)) 



if __name__=='__main__':
	ogr2ogr()