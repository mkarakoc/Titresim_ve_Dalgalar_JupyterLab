# -*- coding: utf-8 -*-
# ****************************************************
# disable all python warnings
# https://stackoverflow.com/questions/14463277/how-to-disable-python-warnings
# python -W ignore foo.py
import warnings
warnings.filterwarnings("ignore")
# ****************************************************
#
# ****************************************************
# Titresim ve Dalgalar ders notlarının
# Jupyter notebooklarında kullanılan ortak kütüphaneler.
# ****************************************************
from ipywidgets import interact, interactive, fixed, interact_manual, FloatSlider
from IPython.display import display, HTML, Markdown, YouTubeVideo, Math
import matplotlib.ticker as tck
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sympy as sym
import scipy
from scipy import integrate # scipy.integrate çalışmadığından bunu da yazdım. (13/2/2019)
from scipy.io import wavfile
import datetime as dt

# ****************************************************
# turn on warnings
# warnings.filterwarnings("once")
# ****************************************************

# matplotlib.colors
# https://matplotlib.org/api/colors_api.html
plt_colors =  ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')

params = {
   'axes.titlesize': 24,
   'axes.labelsize': 18,
   'axes.labelweight': 'bold',
   'font.size': 16, 
   'legend.fontsize': 14,
   'xtick.labelsize': 16,
   'xtick.major.size': 10,
   'xtick.major.width': 1.4,
   'xtick.minor.size': 5,
   'xtick.minor.width': 1.4,
   'ytick.labelsize': 16,
   'ytick.major.size': 10,
   'ytick.major.width': 1.4,
   'ytick.minor.size': 5,
   'ytick.minor.width': 1.4,    
   'lines.linewidth': 1.6,
   'lines.markersize': 8,
   'text.usetex': False,
   'mathtext.fontset': 'stix' # \mathbf --> $\mathbf{\Theta_{cm}}$
   #'text.latex.preamble': r'\usepackage{amsmath}'
   #'figure.figsize': [2.5, 4.5]
}
mpl.rcParams.update(params)

def course_title():
    TXT = \
    ur"""
    <b>
    <font size="6" face='bold' color="blue">TİTREŞİM ve DALGAR / FİZ220 </font> 
    <br><br>
    <font size="5">Doç. Dr. Mesut Karakoç </font>
    </b>
    <br><br>
    <font size="4" color="black"> 
    Akdeniz Üniversitesi, Fen Fakültesi, Fizik Bölümü 
    <br>    
    2018 - 2019 Bahar Dönemi 
    </font>
    <br>
    """
    return display(HTML(TXT))

def course_links(prevp, homep, nextp):
    HTMLCode = \
    ur"""
    <!-- ******************************************************** -->
    <!-- **************** Kod hücrelerini sakla ***************** -->
    <!-- ******************************************************** -->
    <!-- https://stackoverflow.com/questions/31517194/how-to-hide-one-specific-cell-input-or-output-in-ipython-notebook -->
    <script> 
    code_show=true; 
    function code_toggle() {
        if (code_show){$('div.input').hide();} else {$('div.input').show();}
        if (code_show){$('div.cell.code_cell.rendered.selected div.input').hide();} 
        else          {$('div.cell.code_cell.rendered.selected div.input').hide();}
        code_show = !code_show }
    $(document).ready(code_toggle);
    </script>
    
    <a href="javascript:code_toggle()" style="text-decoration:none" 
    class="btn btn-default btn-danger btn-large fa fa-toggle-on">
    &nbsp;&nbsp;&nbsp; Kod hücrelerini, KAPAT / AÇ! </a>
    <!-- ######################################################### -->
    <!-- ######################################################### -->
    
    <!-- ********************************************************* -->
    <!-- ****** Trusted Notebookları başlangıçta çalıştır   ****** -->
    <!-- ****** jupyter trust *.ipynb                       ****** -->
    <!-- ****** ile bütün notebooklar güvenilir yapılabilir.****** -->
    <!-- ********************************************************* -->
    <!--https://stackoverflow.com/questions/31984196/ipython-notebook-run-all-cells-on-open -->
    <script>
        // AUTORUN ALL CELLS ON NOTEBOOK-LOAD!
        require(
            ['base/js/namespace', 'jquery'], 
            function(jupyter, $) {
                $(jupyter.events).on("kernel_ready.Kernel", function () {
                    console.log("Auto-running all cells-below...");
                    jupyter.actions.call('jupyter-notebook:run-all-cells-below');
                 // jupyter.actions.call('jupyter-notebook:save-notebook');
                });
            }
        );
    </script>
    <!-- ######################################################### -->
    <!-- ######################################################### -->
    
    <!-- ******************************************************** -->
    <!-- HTML için gerekli stilleri buradan ayarla                -->
    <!-- Bu hücreyi nbextension'dan 'hide input' kullanarak sakla -->
    <!-- ******************************************************** -->
    
    <style>
    table.a, tr.a {text-align: left !important; 
             font-size: 20px;}
    
    table.b {text-align: left !important; 
             font-size: 16px;
             margin: 0;}
    
    tr.b {text-align: left !important;}
    
    td.b {text-align: left !important;}
    
    li {text-align: left;}
    </style>
    <!-- ######################################################### -->
    <!-- ######################################################### -->
    
    <!-- ********************************************************* -->
    <!-- ****** Sayfa yönlendirme butonları                 ****** -->
    <!-- ********************************************************* -->
    &nbsp;&nbsp;&nbsp;&nbsp;
    <tr align='left'>
        <th>
         <a href="%s" target="_blank">
           <button>
           <i class="fa fa-arrow-circle-left fa-2x" style="color: firebrick ; vertical-align: middle"></i> Önceki Sayfa
           </button> 
         </a>
        </th>
        
        <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>    
        
        <th>
         <a href="%s" target="_blank">
           <button>
           <i class="fa fa-home fa-2x" style="color: firebrick ; vertical-align: middle"></i> Ana Sayfa
           </button> 
         </a>
        </th>
        
        <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
        
        <th>
         <a href="%s" target="_blank">
           <button>
           Sonraki Sayfa <i class="fa fa-arrow-circle-right fa-2x" style="color: firebrick ; vertical-align: middle"></i>
           </button>
         </a>
        </th>
    </tr>
    <!-- ######################################################### -->
    <!-- ######################################################### -->
    """
    return display(HTML(HTMLCode%(prevp, homep, nextp)))



# This is a wrapper that take a filename and publish an html <audio> tag to listen to it.
def wavPlayer(filepath):
    """ will display html 5 player for compatible browser

    Parameters :
    ------------
    filepath : relative filepath with respect to the notebook directory ( where the .ipynb are not cwd)
               of the file to play

    The browser need to know how to play wav through html5.

    there is no autoplay to prevent file playing when the browser opens
    """
    
    src = """
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Simple Test</title>
    </head>
    
    <body>
    <audio controls="controls" style="width:600px" >
      <source src="files/%s?flush_cache=true" type="audio/wav" />
      Your browser does not support the audio element.
    </audio>
    %s
    </body>
    """%(filepath, filepath)
    display(HTML(src))

# LaTeX ifadelerini yazdırmak için
def prinTeX(text, label=ur'', number=ur'\nonumber'):
    if label==ur'': label = ur'label' + str(np.random.random()).replace('.','')
    MarkdownText = \
    ur"""\begin{{align}}
         \label{{{label}}}
         {text} {number}
         \end{{align}}
    """.format(text = text, label=label, number=number)
    display(Markdown(MarkdownText))

# sympy ifadelerini yazdırmak için
def printS(sympyObj, formatS=ur'{} = {}', label=ur'', number=ur'\nonumber'):
    sympyObjLatex = tuple([sym.latex(s) for s in sympyObj])
    if len(sympyObjLatex)==1: formatS = ur'{}'
    prinTeX(formatS.format(*sympyObjLatex), number=number)
    
