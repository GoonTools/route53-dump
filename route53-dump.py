import boto3

client = boto3.client('route53')
def route53dump(records_to_query=['CNAME']):
    paginator = client.get_paginator('list_resource_record_sets')
    
    for zone in client.list_hosted_zones()['HostedZones']:
        
        for page in paginator.paginate(HostedZoneId=zone['Id']):
            for record in page['ResourceRecordSets']:

                if record['Type'] in records_to_query:
                    yield (record['Type'], record['Name'])

for obj in route53dump(): print(obj)
