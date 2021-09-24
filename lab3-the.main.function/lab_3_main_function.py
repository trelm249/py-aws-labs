import boto3

client = boto3.client('translate')

def translate_text(): #declare the function
    response = client.translate_text(
            Text='I am learning to code in AWS',
            SourceLanguageCode='en',
            TargetLanguageCode='es'
    )

    print(response)

def main(): # This is the definition of the primary function that calls other functions.
    translate_text() # The translate_text function is called

if __name__=="__main__": # Invoking main
    main()
