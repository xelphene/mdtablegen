
from mdtable.layout import TableLayout
from mdtable.layout import ColumnLayout
from mdtable.rowfactory import RowFactory

def main():
    ts = TableLayout()
    ts.cols['addr'] = ColumnLayout(width=10)
    ts.cols['comment'] = ColumnLayout(width=30)
    
    
    rf = RowFactory(ts)
    
    rf['addr'] = '10.0.0.1'
    rf['comment'] = 'asdf qwer oijgbo oij sdoijije r joiasd aoidjf more moar moaare'
   
    print( 'addr max: %d' % rf.getMaxFieldDataLen('addr') )
    print( 'comment max: %d' % rf.getMaxFieldDataLen('comment'))

    r = rf.nextRow()
    
    print( repr(r.getDataStrForLine('addr',0)) )
    print( repr(r.getDataStrForLine('addr',1)) )
    
    print('///////')
    
    print( repr(r.getDataStrForLine('comment',0)) )
    print( repr(r.getDataStrForLine('comment',1)) )
    print( repr(r.getDataStrForLine('comment',2)) )
    print( repr(r.getDataStrForLine('comment',3)) )

    print('///////')

    
    print( repr(r.getRowLine(0)) )
    print( repr(r.getRowLine(1)) )
    print( repr(r.getRowLine(2)) )
    print( repr(r.getRowLine(3)) )
    
    print('row lines: %d' % r.numLines )

    print('=====================')

    return
    
    hr = HeadRow(colSpec)
    for l in hr.lines:
        print( repr(l) )
    
    for l in tr.lines:
        print( repr(l) ) 
    
    dr = DivRow(colSpec)
    for l in dr.lines:
        print( repr(l) ) 

    

if __name__ == '__main__':
    main()
