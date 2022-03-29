import click
from protocol.redis import redisEXP

logo = r"""
  ____             _               _______  ______  
 / ___| ___  _ __ | |__   ___ _ __| ____\ \/ /  _ \ 
| |  _ / _ \| '_ \| '_ \ / _ \ '__|  _|  \  /| |_) |
| |_| | (_) | |_) | | | |  __/ |  | |___ /  \|  __/ 
 \____|\___/| .__/|_| |_|\___|_|  |_____/_/\_\_|    
            |_|                                    """

@click.command()
@click.option("-s", required="true", help="type of Server(Redis),developing...Will suport more types of Server")
def main(s):
  print(logo)
  if s.lower() == "redis":
    Redis = redisEXP()
    print("--------*Redis*---EXP---------")
    print(Redis.exploit())

if __name__ == "__main__":
  main()