import subprocess


def moja():
    name = "Assetto Corsa Competizione"
    path1 = "C:\\Program Files (x86)\\Steam New\\steamapps\\common\\Assetto Corsa Competizione\\acc.exe"
   # add = subprocess.Popen(
    #    'netsh advfirewall firewall add rule name="' + name + '" dir=in action=allow program= "' + path1 + '" enable=yes profile=any')
    #subprocess.Popen('')
    #add=subprocess.Popen('netsh advfirewall firewall add rule name="' + name + '" dir=in action=allow program= "' + path1 + '" enable=yes profile=any')
    show=subprocess.Popen('netsh advfirewall firewall show rule name="' + name + '"')
    print(show)
    if not show:
        print("123")
        add = subprocess.Popen('netsh advfirewall firewall add rule name="' + name + '" dir=in action=allow program= "' + path1 + '" enable=yes profile=any')
    delete = subprocess.Popen('netsh advfirewall firewall delete rule name="' + name)


    # XXX{"add" if name!=name else "delete"}
#C:\Program Files (x86)\Steam New\steamapps\common\Assetto Corsa Competizione\acc.exe
    #Assetto Corsa Competizione

if __name__ == '__main__':
  #  check_admin()
    moja()


  #  add_rule("RULE_NAME", "PATH_TO_FILE")
