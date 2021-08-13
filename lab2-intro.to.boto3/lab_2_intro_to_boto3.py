import boto3

client = boto3.client('translate')

def translate_text(): #declare the function
    response = client.translate_text(
            Text='I am learning to code in AWS',
            SourceLanguageCode='en',
            TargetLanguageCode='es'
    )

    print(response)

translate_text()
