import subprocess 


def execute_command():
    #cd services/myscrapper && scrapy crawl entreprise -o result.csv
    # ou importer le programme run ... avec sitemap et file / donner le nom du job au fichier ou pas
    process = subprocess.Popen(['ls', '-l'],
                           stdout=subprocess.PIPE,
                           universal_newlines=True )
    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break