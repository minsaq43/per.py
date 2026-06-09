import pywhatkit as pw
txt = """Human anatomy (gr. ἀνατομία, "dissection", from ἀνά, "up", and τέμνειν, "cut") is primarily the scientific study of the morphology of the human body.
 Anatomy is subdivided into gross anatomy and microscopic anatomy.
 Gross anatomy (also called macroscopic anatomy, topographical anatomy, regional anatomy, or anthropotomy) is the study of anatomical structures that can be seen by the naked eye."""

pw.text_to_handwriting(txt, "Minsa.png",[0,0,138])
print("End")