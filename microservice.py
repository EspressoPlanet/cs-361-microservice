import json
import subprocess
import time



def in_service():
    while True:
        f = open("service.json", "r")
        data = json.load(f)
        if data["request"] == "True":
            out_service()
        else:
            time.sleep(1)
            print("... Waiting for request ...")
            in_service()

def out_service():
    path = "/etc/ssh/ssh_config"
    command = f"cat {path} | tr -d '\n'"
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    dictionary = {"request":"False", "data":process.stdout}
    with open("service.json", "w") as out_serv:
        json.dump(dictionary, out_serv)

def main():

    in_service()

if __name__ == '__main__':
    main()