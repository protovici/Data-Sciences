

import PyPDF2 as pypdf
def findInDict(needle, haystack):
    for key in haystack.keys():
        try:
            value=haystack[key]
        except:
            continue
        if key==needle:
            return value
        if isinstance(value,dict):            
            x=findInDict(needle,value)            
            if x is not None:
                return x
pdfobject=open('C:\Data Sciences','rb')
pdf=pypdf.PdfFileReader(pdfobject)
xfa=findInDict('/doc13908520220126165649.pdf',pdf.resolvedObjects)
xml=xfa[7].getObject().getData()