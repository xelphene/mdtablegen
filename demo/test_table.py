
from mdtablegen.table import MarkdownTable

def main():
    mdt = MarkdownTable()
    
    mdt.addCol('addr')
    mdt.cols['addr'].maxWidth = 15

    mdt.startDiv = '-'
    mdt.headerDiv = '='
    mdt.rowDiv = '-'
    
    mdt.addCol(
        key='comment',
        title='Comment',
        maxWidth = 30
    )
    
    mdt.addRow({
        'addr': '10.0.0.1',
        'comment': 'blah'
    })
    mdt.addRow({
        'addr': '10.0.0.2',
        'comment': 'asdf qwer oijgbo oij sdoijije r joiasd aoidjf more moar moaare'
    })

    #print( mdt.calcColWidths() )    
    
    for line in mdt.render():
        print(line)
    
    
if __name__ == '__main__':
    main()
