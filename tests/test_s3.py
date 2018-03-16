from pgbackup import storage
import boto3


client = boto3.client('s3')
infile = open('example.txt', 'rb')

storage.s3(client, infile, 'pgbackup-swapnasheel', infile.name)

