
# TODO

## soon

## later

### misc

Add something to DividerFactory to implement MD table justification

write tests against prior sanitized segmentation test reports.

### other data inputs

rename MarkdownTable.addRow() to addData()

accept lists. assume data are in the same order as columns were added.

accept iterators (i.e. from csvfile)


# Done

- create a DividerFactory:
  - like RowFactory. takes a TableLayout + ColumnLayouts
  - getSimpleDivider(char)
    - returns a Divider, which acts like a RenderedRow
    - has 'lines' property yields rendered line strings, like RenderedRow
  - getHeaderDivider()
    - heeds MD table justification rules

Rename. 'mdtable' is already taken per pypi. Rename to mdtablegen.

MarkdownTable.render() should yield the lines, not print() them.
