
# TODO

Add something to DividerFactory to implement MD table justification

# Done

- create a DividerFactory:
  - like RowFactory. takes a TableLayout + ColumnLayouts
  - getSimpleDivider(char)
    - returns a Divider, which acts like a RenderedRow
    - has 'lines' property yields rendered line strings, like RenderedRow
  - getHeaderDivider()
    - heeds MD table justification rules
