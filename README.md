# PDF2Booklet
This program reorders the pages of a PDF so that when printed, it stitches the stack of pages together by folding them in half to form a book. To print the cover in color and the rest in black and white, you can separate the outermost page by selecting the "save cover separately" option. This allows for very cheap printing up to 50 pages or even more, whether for autoconsumption or for distribution.

##Attributions:
This program has been made using Qt Designer and the libraries PyPDF2 and PySide6. You can find more projects at https://github.com/vicent-b

##Information:
This program reorders the pages of a PDF so that when printed, it stitches the stack of pages together by folding them in half to form a book. Since the number of pages must be a multiple of 4, inserting pages is allowed. To print the cover in color and the rest in black and white, you can separate the outermost page by selecting the "save cover separately" option.

To print, you must set the printer to 2 pages per sheet, double-sided and to turn the page on the short edge.

To bind, you can:
1) Staple the folded pages on the outside.

2) Staple the folded pages so that the staple closure is on the inside of the book. This may require a particularly long stapler.

3) Imitate method 2 by punching two pairs of holes and tying thread in two loops. It takes more time, but the page can be folded 180° (front cover touching back cover) without breaking.

##Requirements and installation:
To use the source, you need to install Python and, using pip, install PyPDF2 and PySide6. In Windows x64, you may just use the .exe you can find in the "bin" folder.
