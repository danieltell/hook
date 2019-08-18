def hook_graph():
    import clipboard
    html = clipboard.paste()
    if html[:4] != '<div':
        print('hmmm... it seems you didn\'t get the innerHTML correctly!')
        return -1
    new_html = ''
    for i in range(len(html)):
        if html[i] == '<' and html[i+1] == 'i' and html[i+2] == 'm':
            x = i
            while(html[x] != '>'):
                new_html += html[x]
                x += 1
            new_html += '>'
        elif html[i] == '<' and html[i+1] == 'p' and html[i+2] == 'r' and html[i+4] == '>':
            x = i
            while(html[x] != '/'):
                new_html += html[x]
                x += 1
            new_html += '/pre>'
    new_html = "<link rel='stylesheet' type='text/css' href='styles.css'>" + new_html        
    new_html = "<img src='ss.png'>" + new_html
    f = open('/mnt/c/Users/beringela/Desktop/page/result.html', 'w+')  #Path need to be changed
    f.write(new_html)
    f.close()

hook_graph()
