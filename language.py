#Language ID
# 0=Català 1=Castellano 2=English 3=Xertolí

#        1         2         3         4         5         6         7         8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#-------------------------------------------------------------------------------


strLang_TabMain=["Principal", "Principal", "Main"]
strLang_TabInfo=["Informació i acreditacions", "Información y acreditaciones", "Information and credits"]







#===============================================================================

strLang_LoadFile= ["CARREGA L'ARXIU",
                    "CARGA EL ARCHIVO",
                    "LOAD FILE"]

#-------------------------------------------------------------------------------


strLang_InsertText= ["Insereix pàgines en blanc rere la pàgina número:",
                     "Inserta páginas en blanco tras la página número:",
                     "Insert blank pages after page number:"]


strLang_InsertInstructionText= ["(separades per comes i poden repetir-se, usa el signe negatiu per a contar des de raere \ni usa el 0 per a ficar-la davant de tot)",
                                "(separadas mediante comas y pueden repetirse, usa el signo negativo para contar desde \nel final y usa el 0 para insertarla delante de todo)",
                                "(separated by commas, you may repeat page numbers, use negative sign to count from the \nback and use 0 to insert blank page at front)"]


strLang_Convert_NoReorder= ["Convertir sense reordenar", 
                            "Convertir sin reordenar",
                            "Convert without reordering"]


#-------------------------------------------------------------------------------

strLang_NpagesOriginalText=["Número de pàgines original:", 
                      "Número de páginas original:",
                      "Original number of pages:"]

strLang_NpagesInsertedText=["Número de pàgines afegides:",
                            "Número de páginas añadidas:",
                            "Number of inserted pages:"]

strLang_ValidText= ["És vàlid?:",
                    "¿Es válido?:",
                    "Is it valid?:"]



strLang_Valid_Yes= ["Sí, el número de pàgines és múltiple de 4",
                    "Sí, el número de páginas es múltiplo de 4",
                    "Yes, the number of pages is a multiple of 4"]

strLang_Valid_No= ["No, el número de pàgines ha de ser múltiple de 4",
                    "No, el número de páginas debe ser múltiplo de 4",
                    "Yes, the number of pages is a multiple of 4"]

#-------------------------------------------------------------------------------

strLang_Save_Whole= ["Guarda en un sol arxiu",
                    "Guarda en un solo archivo",
                    "Save in a single file"]

strLang_Save_Separately= ["Guarda la portada per separat", 
                          "Guarda la portada por separado", 
                          "Save cover separately"]

strLang_Convert= ["CONVERTIR",
                  "CONVERTIR",
                  "CONVERT"]


#-------------------------------------------------------------------------------

#===============================================================================
#ERRORS

strLang_ERROR_NoErrors=["","",""]

strLang_ERROR_NoFileLoaded= ["ERROR: Ha de carregar un arxiu",
                             "ERROR: Debe cargar un archivo",
                             "ERROR: You must load a file"]

strLang_ERROR_InsertNotValid=["ERROR: La llista de pàgines en blanc que cal inserir ha de ser expressada com a nombres sencers separats per comes",
                             "ERROR: La lista de páginas en blanco a insertar debe estar expresada como número enteros separados por comas",
                             "ERROR: The list of blank pages to insert must be expressed as integers separated by commas"]

strLang_ERROR_Npages= ["ERROR: No es pot reordenar per a imprimir: el nombre de pàgines no és múltiple de 4",
                       "ERROR: No se puede reordenar para imprimir: el número de páginas no es múltiplo de 4",
                       "ERROR: It is not possible to reorder for printing: the number of pages must be a multiple of 4"]

strLang_ERROR_InsertOutOfBounds=["ERROR: Les posicions on inserir la llista de pàgines en blanc no poden ser superiors al número de pàgines, ni en positiu ni en negatiu",
                                 "ERROR: Las posiciones donde insertar las páginas en blanco no pueden exceder el número de páginas, ni en positivo ni en negativo",
                                 "ERROR: The positions where to insert blank pages can not exceed the number of pages, neither as positive nor as negative numbers"]

strLang_ERROR_PyPDF2Failed= ["ERROR: La llibrería que usem per a processar el PDF (PyPDF2) ha fallat per a este arxiu. Prova a generar un nou PDF imprimit l'arxiu com a PDF. No puc fer res més :(",
                             "ERROR: La librería que usamos para procesar el PDF (PyPDF2) ha fallado para este archivo. Prueba a generar un nuevo PDF imprimiendo el archivo como PDF. No puedo hacer nada más :(",
                             "ERROR: The library we use to process the PDF file (PyPDF2) has failed for this file. Try to generate another PDF printing the file as a PDF. I can't do much more :("]




ERROR_MessageTable=[strLang_ERROR_NoErrors, strLang_ERROR_NoFileLoaded, strLang_ERROR_InsertNotValid, strLang_ERROR_Npages, strLang_ERROR_InsertOutOfBounds, strLang_ERROR_PyPDF2Failed]