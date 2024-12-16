
import json

if __name__ == '__main__':

    version = 1204
    io = open(f".\\emcf\\db\\{version}.json", 'w')
    
    selectors = ["@p", "@r", "@a", "@e", "@s"]
    io.write(json.dumps(selectors) + '\n')

    io.close()
