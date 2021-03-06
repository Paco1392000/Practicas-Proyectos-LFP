def flexsilder():
    f = open('Desktop/LFP_Proyecto2/css/flexslider.css', 'w')
    mensaje = '''#page-title{text-align: center; margin: 20px 0px; font-size: 50px; color: #fff;}
/* SLIDER ==============================*/
.slides,
.slides li,
.slides li img{width: 100%;}
.slides li{margin-bottom: -5px;}
/* PAGINACION =======================*/
.flex-control-nav.flex-control-paging{width: 180px; padding: 20px 0px; display: flex; justify-content: center; align-items: center; align-self: center; list-style: none; position: absolute; bottom: -65px; z-index: 3; margin-left: 0%;}
.flex-control-nav li{display: inline-block; margin: 0 5px;}
.flex-control-nav li a{display: block; text-indent: -9999px; border-radius: 50%;}
.flex-control-nav li a.flex-active{background: #353535;}
/* NAVEGACION ===============*/
.flex-direction-nav{z-index: 3; list-style: none;}
.flex-direction-nav a{display: flex; justify-content: center; align-items: center; text-decoration: none; position: absolute;}
.flex-direction-nav a::before{}
.flex-direction-nav a.flex-next::before{}
.flex-direction-nav .flex-prev{}
.flex-direction-nav .flex-next{}
.flexslider:hover .flex-direction-nav .flex-prev{}
.flexslider:hover .flex-direction-nav .flex-next{}
/* CAPTION ==================*/
.caption{width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; text-align: center; position: absolute; top: 0; z-index: 2;}
.caption h2{font-size: 60px; color: #fff; text-shadow: 3px 3px 2px rgba(000, 000, 000, 0.70);}
/* RESPONSIVE ========== */
@media screen and (max-width: 770px){.flex-direction-nav a{opacity: 1;}.flex-direction-nav .flex-prev{left: 15px;}.flex-direction-nav .flex-next{right: 15px;}.caption h2{font-size: 50px;}}
@media screen and (max-width: 600px){.caption h2{font-size: 40px;}.flexslider{width: 100%; border-radius: 0px; border: none;}.slides li{overflow: hidden;}.slides li img{width: 600px;}.flex-direction-nav a{top: auto;}}
@media screen and (max-width: 450px){.slides li img{transform: translateX(-90px);}#page-title{font-size: 40px;}}'''
    f.write(mensaje)
    f.close()
    
#---------------------------------------------------XXXXXXXXXXXXXXXXX---------------------------------
#---------------------------------------------------XXXXXXXXXXXXXXXXX---------------------------------
#---------------------------------------------------------XXXXX---------------------------------------
#---------------------------------------------------------XXXXX---------------------------------------
#---------------------------------------------------------XXXXX---------------------------------------
#---------------------------------------------------------XXXXX---------------------------------------
#---------------------------------------------------------XXXXX---------------------------------------
#---------------------------------------------------XXXXXXXXXXXXXXXXX---------------------------------
#---------------------------------------------------XXXXXXXXXXXXXXXXX---------------------------------
def index():
    f = open('Desktop/LFP_Proyecto2/css/index.css', 'w')
    mensaje = '''@import url('reset.css');
@import url('fuentes.css');
/*--- Estilos Generales ---*/
body {background: -moz-linear-gradient(top, rgba(45,45,45,1) 0%, rgba(102,102,102,0.99) 20%, rgba(83,83,83,0.99) 31%, rgba(53,53,53,0.99) 49%, rgba(45,45,45,1) 64%, rgba(91,91,91,1) 76%, rgba(89,89,89,1) 77%, rgba(45,45,45,1) 98%, rgba(45,45,45,1) 100%); /* FF3.6-15 */background: -webkit-linear-gradient(top, rgba(45,45,45,1) 0%,rgba(102,102,102,0.99) 20%,rgba(83,83,83,0.99) 31%,rgba(53,53,53,0.99) 49%,rgba(45,45,45,1) 64%,rgba(91,91,91,1) 76%,rgba(89,89,89,1) 77%,rgba(45,45,45,1) 98%,rgba(45,45,45,1) 100%); /* Chrome10-25,Safari5.1-6 */background: linear-gradient(to bottom, rgba(45,45,45,1) 0%,rgba(102,102,102,0.99) 20%,rgba(83,83,83,0.99) 31%,rgba(53,53,53,0.99) 49%,rgba(45,45,45,1) 64%,rgba(91,91,91,1) 76%,rgba(89,89,89,1) 77%,rgba(45,45,45,1) 98%,rgba(45,45,45,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#2d2d2d', endColorstr='#2d2d2d',GradientType=0 ); /* IE6-9 */font-family:Yantramanav-Bold;}
a {text-decoration:none; color:#fff;} a:hover {text-decoration:underline;} #wrap {width:960px; margin:auto; clear:both;}
/*--- HEADER ---*/
header {width:100%; float:left; background: #8f0222; /* Old browsers */background: -moz-linear-gradient(top, #8f0222 32%, #8f0222 32%, #8f0222 45%, #6d0019 60%, #8f0222 74%, #170101 100%); /* FF3.6-15 */background: -webkit-linear-gradient(top, #8f0222 32%,#8f0222 32%,#8f0222 45%,#6d0019 60%,#8f0222 74%,#170101 100%); /* Chrome10-25,Safari5.1-6 */background: linear-gradient(to bottom, #8f0222 32%,#8f0222 32%,#8f0222 45%,#6d0019 60%,#8f0222 74%,#170101 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#8f0222', endColorstr='#170101',GradientType=0 ); /* IE6-9 */box-shadow:0px 3px 5px #000;-moz-box-shadow:0px 3px 5px #000; -webkit-box-shadow:0px 3px 5px #000;}
#subheader {width: 960px; margin:auto;}
#logotipo {float:left; width:300px; padding:10px 0px;}
#logotipo a {font-family:Yantramanav-Bold; font-size:50px; color:#000;}
#logotipo a:hover {text-decoration:none;}
 /*Menu*/
header #subheader nav .menu{width:600px; padding:25px 0px 5px 81%; text-align:right; margin-left: -25%;}
header #subheader nav .menu li {display:inline; font-family:Philosopher-BoldItalic;}
header #subheader nav .menu li a {color:#CCB9B9; padding:8px; border-radius:2px; -moz-border-radius:2px; -webkit-border-radius:2px;}
/*--------------------------------------*/
/* Clearing floats */
.cf :before, .cf:after {content: " "; display: table;}
.cf :after {clear: both;}
.cf {*zoom: 1;}
/* Mini reset, no margins, paddings or bullets */
.menu , .submenu {list-style: none;}
/* Main level */
.menu {/* http://www.red-team-design.com/horizontal-centering-using-css-fit-content-value */width: -moz-fit-content; width: -webkit-fit-content; width: fit-content;}
.menu > li {float: left; position: relative; transform: skewX(25deg);}
.menu a {display: block; text-transform: uppercase; text-decoration: none; font-family: Philosopher-BoldItalic; font-size: 14px;}
.menu li:hover {background: #e74c3c;}
.menu > li > a {transform: skewX(-25deg); padding: 0em 0em;}
/* Dropdown */
.submenu {position: absolute; width: 110px; left: 95%; margin-left: -100px; transform: skewX(-25deg); transform-origin: left top;}
.submenu li {background: rgb(102,0,0); /* Old browsers */background: -moz-linear-gradient(top, rgba(102,0,0,1) 0%, rgba(68,1,0,1) 26%, rgba(68,1,0,1) 26%, rgba(58,0,0,1) 32%, rgba(68,1,0,1) 49%, rgba(68,1,0,1) 49%, rgba(102,0,0,1) 60%, rgba(68,1,0,1) 74%, rgba(102,0,0,1) 100%); /* FF3.6-15 */background: -webkit-linear-gradient(top, rgba(102,0,0,1) 0%,rgba(68,1,0,1) 26%,rgba(68,1,0,1) 26%,rgba(58,0,0,1) 32%,rgba(68,1,0,1) 49%,rgba(68,1,0,1) 49%,rgba(102,0,0,1) 60%,rgba(68,1,0,1) 74%,rgba(102,0,0,1) 100%); /* Chrome10-25,Safari5.1-6 */background: linear-gradient(to bottom, rgba(102,0,0,1) 0%,rgba(68,1,0,1) 26%,rgba(68,1,0,1) 26%,rgba(58,0,0,1) 32%,rgba(68,1,0,1) 49%,rgba(68,1,0,1) 49%,rgba(102,0,0,1) 60%,rgba(68,1,0,1) 74%,rgba(102,0,0,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#660000', endColorstr='#660000',GradientType=0 ); /* IE6-9 */  position: relative; overflow: hidden;     }                       
.submenu > li > a {padding: 0em 0em;  }
.submenu > li::after {content: ''; position: absolute; top: -125%; height: 40%; width: 45%; box-shadow: 0 0 50px rgba(0, 0, 0, .9);    }
/* Odd stuff */
.submenu > li:nth-child(odd){transform: skewX(-25deg) translateX(0);}
.submenu > li:nth-child(odd) > a {transform: skewX(25deg);}
.submenu > li:nth-child(odd)::after {right: -10%;transform: skewX(-25deg) rotate(3deg);}
/* Even stuff */
.submenu > li:nth-child(even){transform: skewX(25deg) translateX(0);}
.submenu > li:nth-child(even) > a {transform: skewX(-25deg);}
.submenu > li:nth-child(even)::after {left: -10%;transform: skewX(25deg) rotate(3deg);}
/* Show dropdown */
.submenu , .submenu li {opacity: 0; visibility: hidden;    }
.submenu li {transition: .2s ease transform;}
.menu > li:hover .submenu,
.menu > li:hover .submenu li {opacity: 1; visibility: visible;/* Permalink - use to edit and share this gradient: http://colorzilla.com/gradient-editor/#eaeaea+0,eaeaea+57,eaeaea+74,eaeaea+88&0.13+3,0+16,0.2+31,0+41,0.2+55,0+80,0.12+86,0+90,0.07+94,0.2+95,0+99 */background: -moz-linear-gradient(top, rgba(234,234,234,0.13) 0%, rgba(234,234,234,0.13) 3%, rgba(234,234,234,0) 16%, rgba(234,234,234,0.2) 31%, rgba(234,234,234,0) 41%, rgba(234,234,234,0.2) 55%, rgba(234,234,234,0.18) 57%, rgba(234,234,234,0.05) 74%, rgba(234,234,234,0) 80%, rgba(234,234,234,0.12) 86%, rgba(234,234,234,0.06) 88%, rgba(234,234,234,0) 90%, rgba(234,234,234,0.07) 94%, rgba(234,234,234,0.2) 95%, rgba(234,234,234,0) 99%); /* FF3.6-15 */background: -webkit-linear-gradient(top, rgba(234,234,234,0.13) 0%,rgba(234,234,234,0.13) 3%,rgba(234,234,234,0) 16%,rgba(234,234,234,0.2) 31%,rgba(234,234,234,0) 41%,rgba(234,234,234,0.2) 55%,rgba(234,234,234,0.18) 57%,rgba(234,234,234,0.05) 74%,rgba(234,234,234,0) 80%,rgba(234,234,234,0.12) 86%,rgba(234,234,234,0.06) 88%,rgba(234,234,234,0) 90%,rgba(234,234,234,0.07) 94%,rgba(234,234,234,0.2) 95%,rgba(234,234,234,0) 99%); /* Chrome10-25,Safari5.1-6 */background: linear-gradient(to bottom, rgba(234,234,234,0.13) 0%,rgba(234,234,234,0.13) 3%,rgba(234,234,234,0) 16%,rgba(234,234,234,0.2) 31%,rgba(234,234,234,0) 41%,rgba(234,234,234,0.2) 55%,rgba(234,234,234,0.18) 57%,rgba(234,234,234,0.05) 74%,rgba(234,234,234,0) 80%,rgba(234,234,234,0.12) 86%,rgba(234,234,234,0.06) 88%,rgba(234,234,234,0) 90%,rgba(234,234,234,0.07) 94%,rgba(234,234,234,0.2) 95%,rgba(234,234,234,0) 99%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#21eaeaea', endColorstr='#00eaeaea',GradientType=0 ); /* IE6-9 */}       
.menu > li:hover .submenu li:nth-child(even){transform: skewX(25deg) translateX(15px);}
.menu > li:hover .submenu li:nth-child(odd){transform: skewX(-25deg) translateX(-15px);}
/*-----------------------------------------*/
/* Dropdown */
.submenu2 {position: absolute; width: 175px; left: 20%; margin-left: -120px; transform: skewX(-25deg); transform-origin: left top;}
.submenu2 li {
  background: rgb(102,0,0); /* Old browsers */
    background: -moz-linear-gradient(top, rgba(102,0,0,1) 0%, rgba(68,1,0,1) 26%, rgba(68,1,0,1) 26%, rgba(58,0,0,1) 32%, rgba(68,1,0,1) 49%, rgba(68,1,0,1) 49%, rgba(102,0,0,1) 60%, rgba(68,1,0,1) 74%, rgba(102,0,0,1) 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(top, rgba(102,0,0,1) 0%,rgba(68,1,0,1) 26%,rgba(68,1,0,1) 26%,rgba(58,0,0,1) 32%,rgba(68,1,0,1) 49%,rgba(68,1,0,1) 49%,rgba(102,0,0,1) 60%,rgba(68,1,0,1) 74%,rgba(102,0,0,1) 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(to bottom, rgba(102,0,0,1) 0%,rgba(68,1,0,1) 26%,rgba(68,1,0,1) 26%,rgba(58,0,0,1) 32%,rgba(68,1,0,1) 49%,rgba(68,1,0,1) 49%,rgba(102,0,0,1) 60%,rgba(68,1,0,1) 74%,rgba(102,0,0,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#660000', endColorstr='#660000',GradientType=0 ); /* IE6-9 */  
  position: relative; overflow: hidden;  
}                       
.submenu2 > li > a {padding: 0em 0em;}
.submenu2 > li::after {content: ''; position: absolute; top: -125%; height: 40%; width: 45%; box-shadow: 0 0 50px rgba(0, 0, 0, .9);    }
/* Odd stuff */
.submenu2 > li:nth-child(odd){transform: skewX(-25deg) translateX(0);}
.submenu2 > li:nth-child(odd) > a {transform: skewX(25deg);}
.submenu > li:nth-child(odd)::after {right: -10%; transform: skewX(-25deg) rotate(3deg);}              
/* Even stuff */
.submenu2 > li:nth-child(even){transform: skewX(25deg) translateX(0);}
.submenu2 > li:nth-child(even) > a {transform: skewX(-25deg);}
.submenu2 > li:nth-child(even)::after {left: -10%;transform: skewX(25deg) rotate(3deg);}
/* Show dropdown */
.submenu2,
.submenu2 li {opacity: 0; visibility: hidden;}
.submenu2 li {transition: .2s ease transform;}
.menu > li:hover .submenu2,/*color del submenu*/
.menu > li:hover .submenu2 li {
  opacity: 20; visibility: visible;
  /* Permalink - use to edit and share this gradient: http://colorzilla.com/gradient-editor/#eaeaea+0,eaeaea+57,eaeaea+74,eaeaea+88&0.13+3,0+16,0.2+31,0+41,0.2+55,0+80,0.12+86,0+90,0.07+94,0.2+95,0+99 */
background: -moz-linear-gradient(top, rgba(234,234,234,0.13) 0%, rgba(234,234,234,0.13) 3%, rgba(234,234,234,0) 16%, rgba(234,234,234,0.2) 31%, rgba(234,234,234,0) 41%, rgba(234,234,234,0.2) 55%, rgba(234,234,234,0.18) 57%, rgba(234,234,234,0.05) 74%, rgba(234,234,234,0) 80%, rgba(234,234,234,0.12) 86%, rgba(234,234,234,0.06) 88%, rgba(234,234,234,0) 90%, rgba(234,234,234,0.07) 94%, rgba(234,234,234,0.2) 95%, rgba(234,234,234,0) 99%); /* FF3.6-15 */
background: -webkit-linear-gradient(top, rgba(234,234,234,0.13) 0%,rgba(234,234,234,0.13) 3%,rgba(234,234,234,0) 16%,rgba(234,234,234,0.2) 31%,rgba(234,234,234,0) 41%,rgba(234,234,234,0.2) 55%,rgba(234,234,234,0.18) 57%,rgba(234,234,234,0.05) 74%,rgba(234,234,234,0) 80%,rgba(234,234,234,0.12) 86%,rgba(234,234,234,0.06) 88%,rgba(234,234,234,0) 90%,rgba(234,234,234,0.07) 94%,rgba(234,234,234,0.2) 95%,rgba(234,234,234,0) 99%); /* Chrome10-25,Safari5.1-6 */
background: linear-gradient(to bottom, rgba(234,234,234,0.13) 0%,rgba(234,234,234,0.13) 3%,rgba(234,234,234,0) 16%,rgba(234,234,234,0.2) 31%,rgba(234,234,234,0) 41%,rgba(234,234,234,0.2) 55%,rgba(234,234,234,0.18) 57%,rgba(234,234,234,0.05) 74%,rgba(234,234,234,0) 80%,rgba(234,234,234,0.12) 86%,rgba(234,234,234,0.06) 88%,rgba(234,234,234,0) 90%,rgba(234,234,234,0.07) 94%,rgba(234,234,234,0.2) 95%,rgba(234,234,234,0) 99%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#21eaeaea', endColorstr='#00eaeaea',GradientType=0 ); /* IE6-9 */
}       
.menu > li:hover .submenu2 li:nth-child(even){transform: skewX(25deg) translateX(15px);   }
.menu > li:hover .submenu2 li:nth-child(odd){transform: skewX(-25deg) translateX(-15px);    }
/*---------------------------------------------*/
header #subheader nav ul li a:hover {
  color:#fff;
  /* Permalink - use to edit and share this gradient: http://colorzilla.com/gradient-editor/#5e2129+0,9b111e+2,721422+12,5e2129+19,9b111e+24,721422+36,9b111e+47,5e2129+53,9b111e+63,5e2129+72,721422+87,5e2129+90,9b111e+95,721422+99 */
  background: rgb(91,0,10); /* Old browsers */
  background: -moz-linear-gradient(top, rgba(91,0,10,1) 0%, rgba(153,0,12,1) 3%, rgba(112,0,14,1) 13%, rgba(91,0,10,1) 18%, rgba(153,0,12,1) 24%, rgba(153,0,12,1) 38%, rgba(153,0,12,1) 46%, rgba(153,0,12,1) 46%, rgba(91,0,10,1) 54%, rgba(153,0,12,1) 63%, rgba(91,0,10,1) 75%, rgba(112,0,14,1) 87%, rgba(91,0,10,1) 93%, rgba(153,0,12,1) 94%, rgba(112,0,14,1) 100%); /* FF3.6-15 */
  background: -webkit-linear-gradient(top, rgba(91,0,10,1) 0%,rgba(153,0,12,1) 3%,rgba(112,0,14,1) 13%,rgba(91,0,10,1) 18%,rgba(153,0,12,1) 24%,rgba(153,0,12,1) 38%,rgba(153,0,12,1) 46%,rgba(153,0,12,1) 46%,rgba(91,0,10,1) 54%,rgba(153,0,12,1) 63%,rgba(91,0,10,1) 75%,rgba(112,0,14,1) 87%,rgba(91,0,10,1) 93%,rgba(153,0,12,1) 94%,rgba(112,0,14,1) 100%); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(to bottom, rgba(91,0,10,1) 0%,rgba(153,0,12,1) 3%,rgba(112,0,14,1) 13%,rgba(91,0,10,1) 18%,rgba(153,0,12,1) 24%,rgba(153,0,12,1) 38%,rgba(153,0,12,1) 46%,rgba(153,0,12,1) 46%,rgba(91,0,10,1) 54%,rgba(153,0,12,1) 63%,rgba(91,0,10,1) 75%,rgba(112,0,14,1) 87%,rgba(91,0,10,1) 93%,rgba(153,0,12,1) 94%,rgba(112,0,14,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#5b000a', endColorstr='#70000e',GradientType=0 ); /* IE6-9 */
  text-decoration:none;
}
/*--- MAIN ---*/
#main {width:100%; margin:20px 0px 0px 0px; float:left;}
/*Slideshow*/
#slideshow {width:920px; height:510px; float:left; background:#000; border:solid 20px #fff; margin-bottom:10px;}
#slideshow .pagination {margin:26px auto; width:100px;}
#slideshow .pagination li {float:left; margin:0px 5px; list-style:none;}
#slideshow img {width:920px; height:510px;}
#slideshow .pagination li a {
  display:block; width:12px; height:0px; padding-top:12px;
  background: -moz-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(239,239,239,1) 8%, rgba(239,239,239,0.99) 23%, rgba(227,227,227,0.98) 47%, rgba(226,226,226,0.98) 48%, rgba(239,239,239,0.98) 57%, rgba(226,226,226,0.98) 59%, rgba(239,239,239,0.99) 75%, rgba(226,226,226,1) 92%, rgba(255,255,255,1) 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(top, rgba(255,255,255,1) 0%,rgba(239,239,239,1) 8%,rgba(239,239,239,0.99) 23%,rgba(227,227,227,0.98) 47%,rgba(226,226,226,0.98) 48%,rgba(239,239,239,0.98) 57%,rgba(226,226,226,0.98) 59%,rgba(239,239,239,0.99) 75%,rgba(226,226,226,1) 92%,rgba(255,255,255,1) 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(to bottom, rgba(255,255,255,1) 0%,rgba(239,239,239,1) 8%,rgba(239,239,239,0.99) 23%,rgba(227,227,227,0.98) 47%,rgba(226,226,226,0.98) 48%,rgba(239,239,239,0.98) 57%,rgba(226,226,226,0.98) 59%,rgba(239,239,239,0.99) 75%,rgba(226,226,226,1) 92%,rgba(255,255,255,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#ffffff',GradientType=0 ); /* IE6-9 */
  float:left; overflow:hidden; border-radius:10px; -moz-border-radius:10px; -webkit-border-radius:10px;
}
#slideshow .pagination li.current a {background:#1798af;}
/*---Bienvenidos---*/
#bienvenidos{
  width:920px; float:left; padding:20px;
  background: -moz-linear-gradient(top, rgba(142,112,2,0.98) 0%, rgba(123,95,1,0.98) 9%, rgba(81,57,0,0.98) 29%, rgba(81,57,0,0.99) 56%, rgba(142,112,2,1) 80%, rgba(81,57,0,1) 99%, rgba(81,57,0,1) 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(top, rgba(142,112,2,0.98) 0%,rgba(123,95,1,0.98) 9%,rgba(81,57,0,0.98) 29%,rgba(81,57,0,0.99) 56%,rgba(142,112,2,1) 80%,rgba(81,57,0,1) 99%,rgba(81,57,0,1) 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(to bottom, rgba(142,112,2,0.98) 0%,rgba(123,95,1,0.98) 9%,rgba(81,57,0,0.98) 29%,rgba(81,57,0,0.99) 56%,rgba(142,112,2,1) 80%,rgba(81,57,0,1) 99%,rgba(81,57,0,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#fa8e7002', endColorstr='#513900',GradientType=0 ); /* IE6-9 */
  margin:20px 0px; border-radius:5px;
    -moz-border-radius:5px;   -webkit-border-radius:5px;
  box-shadow:0px 2px 2px #000;
    -moz-box-shadow:0px 2px 2px #000;   -webkit-box-shadow:0px 2px 2px #000;
}
#supah{margin-top: 0%; margin-left: 68%;}
#supah .imagen{width: 80%; height: 50%; border-radius: 0.5em; margin: -43% 0% 0% 0%; align-content: : right;}
#bienvenidos article #supeh{text-align: left; width: 60%; color: #000000; text-decoration: none; margin: 1% 0% 0% 3%;}
#bienvenidos  article h3{font-family:Pattaya-Regular; color:#fff; font-size:40px; margin-bottom:10px;}
#bienvenidos  article ul li{font-family: ElMessiri-Medium;}
#bienvenidos article ul li a:hover{text-decoration: none;}
#bienvenidos article {color:#fff; line-height:27px;}
/*contenido*/ 
#contenido {width:100%; float:left;}
#contenido article {
  float:left; margin-bottom:20px; font-family: Philosopher-BoldItalic; font-size: 20px; background: #000000; /* Old browsers */
  background: -moz-radial-gradient(center, ellipse cover, #000000 6%, #111111 8%, #111111 8%, #111111 14%, #111111 30%, #000000 30%, #000000 42%, #111111 42%, #111111 56%, #000000 56%, #000000 69%, #111111 69%, #111111 80%, #111111 80%, #000000 80%, #000000 80%, #000000 86%, #111111 86%); /* FF3.6-15 */
  background: -webkit-radial-gradient(center, ellipse cover, #000000 6%,#111111 8%,#111111 8%,#111111 14%,#111111 30%,#000000 30%,#000000 42%,#111111 42%,#111111 56%,#000000 56%,#000000 69%,#111111 69%,#111111 80%,#111111 80%,#000000 80%,#000000 80%,#000000 86%,#111111 86%); /* Chrome10-25,Safari5.1-6 */
  background: radial-gradient(ellipse at center, #000000 6%,#111111 8%,#111111 8%,#111111 14%,#111111 30%,#000000 30%,#000000 42%,#111111 42%,#111111 56%,#000000 56%,#000000 69%,#111111 69%,#111111 80%,#111111 80%,#000000 80%,#000000 80%,#000000 86%,#111111 86%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#000000', endColorstr='#111111',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
}
  #contenido article .titulo {
  font-size:25px; font-family:Voltaire-Medium; color:#fff; text-align: center; background: #230203; /* Old browsers */
  background: -moz-radial-gradient(center, ellipse cover, #230203 0%, #560506 5%, #230203 10%, #560506 18%, #230203 20%, #560506 26%, #230203 30%, #560506 36%, #230203 41%, #560506 46%, #230203 52%, #560506 55%, #230203 61%, #560506 71%, #230203 80%, #560506 90%, #230203 99%); /* FF3.6-15 */
  background: -webkit-radial-gradient(center, ellipse cover, #230203 0%,#560506 5%,#230203 10%,#560506 18%,#230203 20%,#560506 26%,#230203 30%,#560506 36%,#230203 41%,#560506 46%,#230203 52%,#560506 55%,#230203 61%,#560506 71%,#230203 80%,#560506 90%,#230203 99%); /* Chrome10-25,Safari5.1-6 */
  background: radial-gradient(ellipse at center, #230203 0%,#560506 5%,#230203 10%,#560506 18%,#230203 20%,#560506 26%,#230203 30%,#560506 36%,#230203 41%,#560506 46%,#230203 52%,#560506 55%,#230203 61%,#560506 71%,#230203 80%,#560506 90%,#230203 99%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#230203', endColorstr='#230203',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
  border-radius:5px; margin: 0px 2px;  border: #230606 groove; border-radius: 5px;
} 
#contenido article .fecha {font-size:18px; color:#1798af; margin-bottom:5px; margin-left: 234px; border-radius: 5px;}
#contenido article .thumb {width:190px; height:190px; float:left; margin: 0px 10px 10px 5px; border-radius: 5px; border:solid 1px #111;}
#contenido article > p {color:#8c8c8c; font-size:14px; text-align:justify; margin: 5px 10px 5px 10px;}
/*---Sidebar---*/
aside{
  width:220px; float:left; margin-left:20px; background: #8f0222; /* Old browsers */
    background: -moz-linear-gradient(top, #8f0222 32%, #8f0222 32%, #8f0222 45%, #6d0019 60%, #8f0222 74%, #170101 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(top, #8f0222 32%,#8f0222 32%,#8f0222 45%,#6d0019 60%,#8f0222 74%,#170101 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(to bottom, #8f0222 32%,#8f0222 32%,#8f0222 45%,#6d0019 60%,#8f0222 74%,#170101 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#8f0222', endColorstr='#170101',GradientType=0 ); /* IE6-9 */
  padding:10px 10px 0px 10px; border-radius:5px;
    -moz-border-radius:5px;   -webkit-border-radius:5px;
  box-shadow:0px 2px 2px #000;
    -moz-box-shadow:0px 2px 2px #000;    -webkit-box-shadow:0px 2px 2px #000;
}
aside .widget {margin-bottom:10px; float:left;}
aside .widget > h3 {
  background: -moz-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(239,239,239,1) 8%, rgba(239,239,239,0.99) 23%, rgba(227,227,227,0.98) 47%, rgba(226,226,226,0.98) 48%, rgba(239,239,239,0.98) 57%, rgba(226,226,226,0.98) 59%, rgba(239,239,239,0.99) 75%, rgba(226,226,226,1) 92%, rgba(255,255,255,1) 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(top, rgba(255,255,255,1) 0%,rgba(239,239,239,1) 8%,rgba(239,239,239,0.99) 23%,rgba(227,227,227,0.98) 47%,rgba(226,226,226,0.98) 48%,rgba(239,239,239,0.98) 57%,rgba(226,226,226,0.98) 59%,rgba(239,239,239,0.99) 75%,rgba(226,226,226,1) 92%,rgba(255,255,255,1) 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(to bottom, rgba(255,255,255,1) 0%,rgba(239,239,239,1) 8%,rgba(239,239,239,0.99) 23%,rgba(227,227,227,0.98) 47%,rgba(226,226,226,0.98) 48%,rgba(239,239,239,0.98) 57%,rgba(226,226,226,0.98) 59%,rgba(239,239,239,0.99) 75%,rgba(226,226,226,1) 92%,rgba(255,255,255,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#ffffff',GradientType=0 ); /* IE6-9 */
  color:#4d78b3; width:220px; padding:10px 0px; text-align:center; font-weight:bold; margin-bottom:10px;
}
aside .widget ul li a:hover{
  text-decoration:none;
  background: #440102; /* Old browsers */
  background: -moz-radial-gradient(center, ellipse cover, #440102 0%, #770204 2%, #440102 5%, #770204 8%, #440102 10%, #440102 11%, #770204 13%, #440102 16%, #440102 19%, #770204 22%, #440102 26%, #440102 37%, #770204 39%, #440102 43%, #440102 49%, #770204 57%, #440102 59%, #440102 63%, #770204 67%, #770204 67%, #440102 68%, #440102 73%, #770204 73%, #770204 80%, #440102 83%, #440102 87%, #770204 90%, #440102 94%, #440102 100%); /* FF3.6-15 */
  background: -webkit-radial-gradient(center, ellipse cover, #440102 0%,#770204 2%,#440102 5%,#770204 8%,#440102 10%,#440102 11%,#770204 13%,#440102 16%,#440102 19%,#770204 22%,#440102 26%,#440102 37%,#770204 39%,#440102 43%,#440102 49%,#770204 57%,#440102 59%,#440102 63%,#770204 67%,#770204 67%,#440102 68%,#440102 73%,#770204 73%,#770204 80%,#440102 83%,#440102 87%,#770204 90%,#440102 94%,#440102 100%); /* Chrome10-25,Safari5.1-6 */
  background: radial-gradient(ellipse at center, #440102 0%,#770204 2%,#440102 5%,#770204 8%,#440102 10%,#440102 11%,#770204 13%,#440102 16%,#440102 19%,#770204 22%,#440102 26%,#440102 37%,#770204 39%,#440102 43%,#440102 49%,#770204 57%,#440102 59%,#440102 63%,#770204 67%,#770204 67%,#440102 68%,#440102 73%,#770204 73%,#770204 80%,#440102 83%,#440102 87%,#770204 90%,#440102 94%,#440102 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#440102', endColorstr='#440102',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
}
aside .widget a {color:#fff; padding-left: 5px; padding-right: 9px;}
aside .widget ul li {margin-bottom:5px;}
aside .widget img {width:220px;}
/*-------------*/
#as2 {
  margin-top: 40px; width:220px; float:left; margin-left:20px; background: #8f0222; /* Old browsers */
    background: -moz-linear-gradient(top, #8f0222 32%, #8f0222 32%, #8f0222 45%, #6d0019 60%, #8f0222 74%, #170101 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(top, #8f0222 32%,#8f0222 32%,#8f0222 45%,#6d0019 60%,#8f0222 74%,#170101 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(to bottom, #8f0222 32%,#8f0222 32%,#8f0222 45%,#6d0019 60%,#8f0222 74%,#170101 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#8f0222', endColorstr='#170101',GradientType=0 ); /* IE6-9 */
  padding:10px 10px 0px 10px; border-radius:5px;
    -moz-border-radius:5px;   -webkit-border-radius:5px;
  box-shadow:0px 2px 2px #000;
    -moz-box-shadow:0px 2px 2px #000;   -webkit-box-shadow:0px 2px 2px #000;
}
#as2 .widget {margin-bottom:10px; float:left;}
#as2 .widget > h3 {
  background: -moz-linear-gradient(top, rgba(255,255,255,1) 0%, rgba(239,239,239,1) 8%, rgba(239,239,239,0.99) 23%, rgba(227,227,227,0.98) 47%, rgba(226,226,226,0.98) 48%, rgba(239,239,239,0.98) 57%, rgba(226,226,226,0.98) 59%, rgba(239,239,239,0.99) 75%, rgba(226,226,226,1) 92%, rgba(255,255,255,1) 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(top, rgba(255,255,255,1) 0%,rgba(239,239,239,1) 8%,rgba(239,239,239,0.99) 23%,rgba(227,227,227,0.98) 47%,rgba(226,226,226,0.98) 48%,rgba(239,239,239,0.98) 57%,rgba(226,226,226,0.98) 59%,rgba(239,239,239,0.99) 75%,rgba(226,226,226,1) 92%,rgba(255,255,255,1) 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(to bottom, rgba(255,255,255,1) 0%,rgba(239,239,239,1) 8%,rgba(239,239,239,0.99) 23%,rgba(227,227,227,0.98) 47%,rgba(226,226,226,0.98) 48%,rgba(239,239,239,0.98) 57%,rgba(226,226,226,0.98) 59%,rgba(239,239,239,0.99) 75%,rgba(226,226,226,1) 92%,rgba(255,255,255,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#ffffff',GradientType=0 ); /* IE6-9 */
  color:#4d78b3; width:220px; padding:10px 0px; text-align:center; font-weight:bold; margin-bottom:10px;
}
#as2 .widget ul li a:hover{
  text-decoration:none; background: #440102; /* Old browsers */
  background: -moz-radial-gradient(center, ellipse cover, #440102 0%, #770204 2%, #440102 5%, #770204 8%, #440102 10%, #440102 11%, #770204 13%, #440102 16%, #440102 19%, #770204 22%, #440102 26%, #440102 37%, #770204 39%, #440102 43%, #440102 49%, #770204 57%, #440102 59%, #440102 63%, #770204 67%, #770204 67%, #440102 68%, #440102 73%, #770204 73%, #770204 80%, #440102 83%, #440102 87%, #770204 90%, #440102 94%, #440102 100%); /* FF3.6-15 */
  background: -webkit-radial-gradient(center, ellipse cover, #440102 0%,#770204 2%,#440102 5%,#770204 8%,#440102 10%,#440102 11%,#770204 13%,#440102 16%,#440102 19%,#770204 22%,#440102 26%,#440102 37%,#770204 39%,#440102 43%,#440102 49%,#770204 57%,#440102 59%,#440102 63%,#770204 67%,#770204 67%,#440102 68%,#440102 73%,#770204 73%,#770204 80%,#440102 83%,#440102 87%,#770204 90%,#440102 94%,#440102 100%); /* Chrome10-25,Safari5.1-6 */
  background: radial-gradient(ellipse at center, #440102 0%,#770204 2%,#440102 5%,#770204 8%,#440102 10%,#440102 11%,#770204 13%,#440102 16%,#440102 19%,#770204 22%,#440102 26%,#440102 37%,#770204 39%,#440102 43%,#440102 49%,#770204 57%,#440102 59%,#440102 63%,#770204 67%,#770204 67%,#440102 68%,#440102 73%,#770204 73%,#770204 80%,#440102 83%,#440102 87%,#770204 90%,#440102 94%,#440102 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#440102', endColorstr='#440102',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
}
#as2 .widget a {color:#fff;padding-left: 5px; padding-right: 9px;}
#as2 .widget ul li {margin-bottom:5px; text-align: right;}
#as2 .widget ul{ margin-top:-250px;}
#as2 .widget .imga {width:162px; height:248px; margin-top:0px;}
#as2 .widget img {width:220px;}
/*Footer*/
footer {
  width:100%; float:left; clear:both; box-shadow:0px 2px 2px #000;
    -moz-box-shadow:0px 2px 2px #000;   -webkit-box-shadow:0px 2px 2px #000;
  border-radius:5px;
    -moz-border-radius:5px;   -webkit-border-radius:5px;
  background: #2f2f2f; /* Old browsers */
background: -moz-linear-gradient(top,  #2f2f2f 0%, #242424 100%); /* FF3.6+ */
background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#2f2f2f), color-stop(100%,#242424)); /* Chrome,Safari4+ */
background: -webkit-linear-gradient(top,  #2f2f2f 0%,#242424 100%); /* Chrome10+,Safari5.1+ */
background: -o-linear-gradient(top,  #2f2f2f 0%,#242424 100%); /* Opera 11.10+ */
background: -ms-linear-gradient(top,  #2f2f2f 0%,#242424 100%); /* IE10+ */
background: linear-gradient(to bottom,  #2f2f2f 0%,#242424 100%); /* W3C */
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#2f2f2f', endColorstr='#242424',GradientType=0 ); /* IE6-9 */
}
footer section {width:440px; float:left; padding:20px;}
footer #acerca-de {font-family:Pattaya-Regular; font-size:13.8px; color:#8c8c8c; text-align:justify; line-height:20px;}
footer #acerca-de h3 {font-family:Ubuntu-MediumItalic; font-size:20px; color:#fff; margin-bottom:5px;}
footer #redes-s > div {width:64px; height:64px; float:left; background:#ff8000; opacity:0.5;}
footer #redes-s > div a {width:64px; height:64px; display:inline-block;}
footer #redes-s .email {background:url(../imagenes/correo.png); margin-bottom:15px;}
footer #redes-s .twitter {background:url(../imagenes/twitter.png); margin-bottom:15px;}
footer #redes-s .facebook {background:url(../imagenes/facebook.png);}
footer #redes-s .youtube {background:url(../imagenes/youtube.png);}
footer #redes-s > div:hover {opacity:1;}
#copyright {float:left; width:960px; margin:10px 0px;}
#copyright p {text-align:center; font-size:12px; color:#fff; font-family:Arial, Helvetica, Sans-serif;}
/*--------------------------*/
.flexslider{border-radius: 8px; box-shadow: 0px 0px 30px 0px rgba(0,0,0,0.70); display: flex; flex-direction: column; position: relative;}
/*Contenido De Bienvenidos*/
#tab-1 .ima{height: 300px; width: 330px; margin-left: 250px; margin-top: -100px;}
#tab-1 ul li a{margin-left: 2.5em;font-family: Philosopher-BoldItalic; font-size: 17px; border-color: aliceblue; color:#000000; padding:0.2em; margin-top:0.05em; margin-bottom: 0.05em; margin-right: 0.05em;}
#tab-1 ul li a:hover{
  border-color:aqua; color:#520406; background: #ffffff; /* Old browsers */
  background: -moz-linear-gradient(top, #ffffff 1%, #d6d6d6 13%, #ffffff 21%, #ffffff 21%, #d6d6d6 29%, #e8e8e8 38%, #d6d6d6 44%, #ffffff 52%, #ffffff 59%, #ffffff 64%, #d6d6d6 68%, #e8e8e8 80%, #d6d6d6 85%, #ffffff 90%, #d6d6d6 97%, #ffffff 100%); /* FF3.6-15 */
  background: -webkit-linear-gradient(top, #ffffff 1%,#d6d6d6 13%,#ffffff 21%,#ffffff 21%,#d6d6d6 29%,#e8e8e8 38%,#d6d6d6 44%,#ffffff 52%,#ffffff 59%,#ffffff 64%,#d6d6d6 68%,#e8e8e8 80%,#d6d6d6 85%,#ffffff 90%,#d6d6d6 97%,#ffffff 100%); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(to bottom, #ffffff 1%,#d6d6d6 13%,#ffffff 21%,#ffffff 21%,#d6d6d6 29%,#e8e8e8 38%,#d6d6d6 44%,#ffffff 52%,#ffffff 59%,#ffffff 64%,#d6d6d6 68%,#e8e8e8 80%,#d6d6d6 85%,#ffffff 90%,#d6d6d6 97%,#ffffff 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#ffffff',GradientType=0 ); border-radius: 0.1em; padding: 0.2em; /* IE6-9 */
}
#tab-2 .ima{width: 80%; margin-left: 95px; margin-top: -100px; border-radius: 0.2em;}
#tab-2 ul li a{font-family: Philosopher-BoldItalic; border-color: aliceblue; color:#000000; padding:0.1em; margin:0.05em;}
#tab-2 ul li a:hover{
  border-color:aqua; color:#520406; background: #ffffff; /* Old browsers */
  background: -moz-linear-gradient(top, #ffffff 1%, #d6d6d6 13%, #ffffff 21%, #ffffff 21%, #d6d6d6 29%, #e8e8e8 38%, #d6d6d6 44%, #ffffff 52%, #ffffff 59%, #ffffff 64%, #d6d6d6 68%, #e8e8e8 80%, #d6d6d6 85%, #ffffff 90%, #d6d6d6 97%, #ffffff 100%); /* FF3.6-15 */
  background: -webkit-linear-gradient(top, #ffffff 1%,#d6d6d6 13%,#ffffff 21%,#ffffff 21%,#d6d6d6 29%,#e8e8e8 38%,#d6d6d6 44%,#ffffff 52%,#ffffff 59%,#ffffff 64%,#d6d6d6 68%,#e8e8e8 80%,#d6d6d6 85%,#ffffff 90%,#d6d6d6 97%,#ffffff 100%); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(to bottom, #ffffff 1%,#d6d6d6 13%,#ffffff 21%,#ffffff 21%,#d6d6d6 29%,#e8e8e8 38%,#d6d6d6 44%,#ffffff 52%,#ffffff 59%,#ffffff 64%,#d6d6d6 68%,#e8e8e8 80%,#d6d6d6 85%,#ffffff 90%,#d6d6d6 97%,#ffffff 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#ffffff',GradientType=0 ); /* IE6-9 */
}
#tab-3 .ima{width: 450px; margin-left: 400px; margin-top: -100px; border-radius: 0.2em;}
#tab-3 ul li a{font-family: Philosopher-BoldItalic; border-color: aliceblue; color:#000000; padding:0.2em; margin:0.05em;}
#tab-3 ul li a:hover{
  border-color:aqua; color:#520406; background: #ffffff; /* Old browsers */
  background: -moz-linear-gradient(top, #ffffff 1%, #d6d6d6 13%, #ffffff 21%, #ffffff 21%, #d6d6d6 29%, #e8e8e8 38%, #d6d6d6 44%, #ffffff 52%, #ffffff 59%, #ffffff 64%, #d6d6d6 68%, #e8e8e8 80%, #d6d6d6 85%, #ffffff 90%, #d6d6d6 97%, #ffffff 100%); /* FF3.6-15 */
  background: -webkit-linear-gradient(top, #ffffff 1%,#d6d6d6 13%,#ffffff 21%,#ffffff 21%,#d6d6d6 29%,#e8e8e8 38%,#d6d6d6 44%,#ffffff 52%,#ffffff 59%,#ffffff 64%,#d6d6d6 68%,#e8e8e8 80%,#d6d6d6 85%,#ffffff 90%,#d6d6d6 97%,#ffffff 100%); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(to bottom, #ffffff 1%,#d6d6d6 13%,#ffffff 21%,#ffffff 21%,#d6d6d6 29%,#e8e8e8 38%,#d6d6d6 44%,#ffffff 52%,#ffffff 59%,#ffffff 64%,#d6d6d6 68%,#e8e8e8 80%,#d6d6d6 85%,#ffffff 90%,#d6d6d6 97%,#ffffff 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#ffffff',GradientType=0 ); border-radius: 0.1em; padding: 0.2em; /* IE6-9 */
}
#tab-4 .ima{width: 80%; margin-left: 95px; border-radius: 0.2em;}
#tab-4 ul li a{font-family: Philosopher-BoldItalic; border-color: aliceblue; color:#000000; padding:0.2em; margin:0.05em;}
#tab-4 ul li a:hover{
  border-color:aqua; color:#520406; background: #ffffff; /* Old browsers */
  background: -moz-linear-gradient(top, #ffffff 1%, #d6d6d6 13%, #ffffff 21%, #ffffff 21%, #d6d6d6 29%, #e8e8e8 38%, #d6d6d6 44%, #ffffff 52%, #ffffff 59%, #ffffff 64%, #d6d6d6 68%, #e8e8e8 80%, #d6d6d6 85%, #ffffff 90%, #d6d6d6 97%, #ffffff 100%); /* FF3.6-15 */
  background: -webkit-linear-gradient(top, #ffffff 1%,#d6d6d6 13%,#ffffff 21%,#ffffff 21%,#d6d6d6 29%,#e8e8e8 38%,#d6d6d6 44%,#ffffff 52%,#ffffff 59%,#ffffff 64%,#d6d6d6 68%,#e8e8e8 80%,#d6d6d6 85%,#ffffff 90%,#d6d6d6 97%,#ffffff 100%); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(to bottom, #ffffff 1%,#d6d6d6 13%,#ffffff 21%,#ffffff 21%,#d6d6d6 29%,#e8e8e8 38%,#d6d6d6 44%,#ffffff 52%,#ffffff 59%,#ffffff 64%,#d6d6d6 68%,#e8e8e8 80%,#d6d6d6 85%,#ffffff 90%,#d6d6d6 97%,#ffffff 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ffffff', endColorstr='#ffffff',GradientType=0 ); border-radius: 0.1em; padding: 0.2em; /* IE6-9 */
}
/*-------------------------*/'''
    f.write(mensaje)
    f.close()
    
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------  
def reset_css():
    f = open('Desktop/LFP_Proyecto2/css/reset.css', 'w')
    mensaje = '''/* --
CSS Reseter
CSSLab ?? 2010 by Jorge Epu??an
http://www.csslab.cl/2010/06/01/css-reseter-v2/
-- */
html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, font, img, ins, kbd, q, s, samp, small, strike, sub, sup, tt, var, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, dialog, figure, header, footer, hgroup, menu, nav, section, time, mark, audio, video {margin: 0;padding: 0;border: 0;outline: 0;font-weight: inherit;font-style: inherit;font-size: 100%;}
article, aside, nav, section, dialog, figure, header, footer, hgroup { display:block;} legend {display:none;}
:focus {outline: 0;}
table {border-collapse: collapse;border-spacing: 0;} caption, th, td {text-align: left;font-weight: normal;} a img, iframe {border: none;}
ul {list-style: none;} input, textarea, select, button {font-size: 100%;font-family: inherit;} input, select {vertical-align:middle;}
select {margin: inherit;} button {border: 0;padding: 0;background: transparent;cursor: pointer;}
/* Fixes incorrect placement of numbers in ol's in IE6/7 */
ol { margin-left:2em; }
/* ========================================= clearfix == */
.clearfix:after {content: ".";display: block;height: 0;clear: both;visibility: hidden;} .clearfix {display: inline-block;}
* html .clearfix {height: 1%;} .clearfix {display: block;}'''
    f.write(mensaje)
    f.close()

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
def fuentes():
    f = open('Desktop/LFP_Proyecto2/css/fuentes.css', 'w')
    mensaje = '''@font-face{font-family:SourceSans;src:url(../fuentes/Source_Sans_Pro/SourceSansPro-Regular.ttf); }
@font-face{font-family:SourceSansPro-Light;src:url(../fuentes/Source_Sans_Pro/SourceSansPro-Light.ttf); }
@font-face{font-family:Philosopher-BoldItalic;src:url(../fuentes/Philosopher/Philosopher-BoldItalic.ttf); }
@font-face{font-family:Yantramanav-Bold;src:url(../fuentes/Yantramanav/Yantramanav-Bold.ttf); }
@font-face{font-family:Pattaya-Regular;src:url(../fuentes/Pattaya/Pattaya-Regular.ttf); }
@font-face{font-family:Voltaire-Regular;src:url(../fuentes/Voltaire/Voltaire-Regular.ttf); }
@font-face{font-family:ElMessiri-Medium;src:url(../fuentes/El_Messiri/ElMessiri-Medium.ttf); }
@font-face{font-family:Ubuntu-MediumItalic;src:url(../fuentes/Ubuntu/Ubuntu-MediumItalic.ttf); }
@font-face {font-family: 'FontAwesome';src: url('../fonts/fontawesome-webfont.eot?v=4.7.0');src: url('../fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');font-weight: normal;font-style: normal;}'''
    f.write(mensaje)
    f.close()

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
def font_awesome():
    f = open('Desktop/LFP_Proyecto2/css/font-awesome.css', 'w')
    mensaje = '''/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eeeeee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #ffffff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
'''
    f.write(mensaje)
    f.close()

#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------   
def jquery_ui():
    f = open('Desktop/LFP_Proyecto2/css/jquery-ui.css', 'w')
    mensaje = '''/*! jQuery UI - v1.12.1 - 2016-09-14
* http://jqueryui.com
* Includes: core.css, accordion.css, autocomplete.css, menu.css, button.css, controlgroup.css, checkboxradio.css, datepicker.css, dialog.css, draggable.css, resizable.css, progressbar.css, selectable.css, selectmenu.css, slider.css, sortable.css, spinner.css, tabs.css, tooltip.css, theme.css
* To view and modify this theme, visit http://jqueryui.com/themeroller/?ffDefault=Arial%2CHelvetica%2Csans-serif&fsDefault=1em&fwDefault=normal&cornerRadius=3px&bgColorHeader=e9e9e9&bgTextureHeader=flat&borderColorHeader=dddddd&fcHeader=333333&iconColorHeader=444444&bgColorContent=ffffff&bgTextureContent=flat&borderColorContent=dddddd&fcContent=333333&iconColorContent=444444&bgColorDefault=f6f6f6&bgTextureDefault=flat&borderColorDefault=c5c5c5&fcDefault=454545&iconColorDefault=777777&bgColorHover=ededed&bgTextureHover=flat&borderColorHover=cccccc&fcHover=2b2b2b&iconColorHover=555555&bgColorActive=007fff&bgTextureActive=flat&borderColorActive=003eff&fcActive=ffffff&iconColorActive=ffffff&bgColorHighlight=fffa90&bgTextureHighlight=flat&borderColorHighlight=dad55e&fcHighlight=777620&iconColorHighlight=777620&bgColorError=fddfdf&bgTextureError=flat&borderColorError=f1a899&fcError=5f3f3f&iconColorError=cc0000&bgColorOverlay=aaaaaa&bgTextureOverlay=flat&bgImgOpacityOverlay=0&opacityOverlay=30&bgColorShadow=666666&bgTextureShadow=flat&bgImgOpacityShadow=0&opacityShadow=30&thicknessShadow=5px&offsetTopShadow=0px&offsetLeftShadow=0px&cornerRadiusShadow=8px
* Copyright jQuery Foundation and other contributors; Licensed MIT */

/* Layout helpers
----------------------------------*/
.ui-helper-hidden {
	display: none;
}
.ui-helper-hidden-accessible {
	border: 0;
	clip: rect(0 0 0 0);
	height: 1px;
	margin: -1px;
	overflow: hidden;
	padding: 0;
	position: absolute;
	width: 1px;
}
.ui-helper-reset {
	margin: 0;
	padding: 0;
	border: 0;
	outline: 0;
	line-height: 1.3;
	text-decoration: none;
	font-size: 100%;
	list-style: none;
}
.ui-helper-clearfix:before,
.ui-helper-clearfix:after {
	content: "";
	display: table;
	border-collapse: collapse;
}
.ui-helper-clearfix:after {
	clear: both;
}
.ui-helper-zfix {
	width: 100%;
	height: 100%;
	top: 0;
	left: 0;
	position: absolute;
	opacity: 0;
	filter:Alpha(Opacity=0); /* support: IE8 */
}

.ui-front {
	z-index: 100;
}


/* Interaction Cues
----------------------------------*/
.ui-state-disabled {
	cursor: default !important;
	pointer-events: none;
}


/* Icons
----------------------------------*/
.ui-icon {
	display: inline-block;
	vertical-align: middle;
	margin-top: -.25em;
	position: relative;
	text-indent: -99999px;
	overflow: hidden;
	background-repeat: no-repeat;
}

.ui-widget-icon-block {
	left: 50%;
	margin-left: -8px;
	display: block;
}

/* Misc visuals
----------------------------------*/

/* Overlays */
.ui-widget-overlay {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}
.ui-accordion .ui-accordion-header {
	display: block;
	cursor: pointer;
	position: relative;
	margin: 2px 0 0 0;
	padding: .5em .5em .5em .7em;
	font-size: 100%;
}
.ui-accordion .ui-accordion-content {
	padding: 1em 2.2em;
	border-top: 0;
	overflow: auto;
}
.ui-autocomplete {
	position: absolute;
	top: 0;
	left: 0;
	cursor: default;
}
.ui-menu {
	list-style: none;
	padding: 0;
	margin: 0;
	display: block;
	outline: 0;
}
.ui-menu .ui-menu {
	position: absolute;
}
.ui-menu .ui-menu-item {
	margin: 0;
	cursor: pointer;
	/* support: IE10, see #8844 */
	list-style-image: url("data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7");
}
.ui-menu .ui-menu-item-wrapper {
	position: relative;
	padding: 3px 1em 3px .4em;
}
.ui-menu .ui-menu-divider {
	margin: 5px 0;
	height: 0;
	font-size: 0;
	line-height: 0;
	border-width: 1px 0 0 0;
}
.ui-menu .ui-state-focus,
.ui-menu .ui-state-active {
	margin: -1px;
}

/* icon support */
.ui-menu-icons {
	position: relative;
}
.ui-menu-icons .ui-menu-item-wrapper {
	padding-left: 2em;
}

/* left-aligned */
.ui-menu .ui-icon {
	position: absolute;
	top: 0;
	bottom: 0;
	left: .2em;
	margin: auto 0;
}

/* right-aligned */
.ui-menu .ui-menu-icon {
	left: auto;
	right: 0;
}
.ui-button {
	padding: .4em 1em;
	display: inline-block;
	position: relative;
	line-height: normal;
	margin-right: .1em;
	cursor: pointer;
	vertical-align: middle;
	text-align: center;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;

	/* Support: IE <= 11 */
	overflow: visible;
}

.ui-button,
.ui-button:link,
.ui-button:visited,
.ui-button:hover,
.ui-button:active {
	text-decoration: none;
}

/* to make room for the icon, a width needs to be set here */
.ui-button-icon-only {
	width: 2em;
	box-sizing: border-box;
	text-indent: -9999px;
	white-space: nowrap;
}

/* no icon support for input elements */
input.ui-button.ui-button-icon-only {
	text-indent: 0;
}

/* button icon element(s) */
.ui-button-icon-only .ui-icon {
	position: absolute;
	top: 50%;
	left: 50%;
	margin-top: -8px;
	margin-left: -8px;
}

.ui-button.ui-icon-notext .ui-icon {
	padding: 0;
	width: 2.1em;
	height: 2.1em;
	text-indent: -9999px;
	white-space: nowrap;

}

input.ui-button.ui-icon-notext .ui-icon {
	width: auto;
	height: auto;
	text-indent: 0;
	white-space: normal;
	padding: .4.5em 1em;
}

/* workarounds */
/* Support: Firefox 5 - 40 */
input.ui-button::-moz-focus-inner,
button.ui-button::-moz-focus-inner {
	border: 0;
	padding: 0;
}
.ui-controlgroup {
	vertical-align: middle;
	display: inline-block;
}
.ui-controlgroup > .ui-controlgroup-item {
	float: left;
	margin-left: 0;
	margin-right: 0;
}
.ui-controlgroup > .ui-controlgroup-item:focus,
.ui-controlgroup > .ui-controlgroup-item.ui-visual-focus {
	z-index: 9999;
}
.ui-controlgroup-vertical > .ui-controlgroup-item {
	display: block;
	float: none;
	width: 100%;
	margin-top: 0;
	margin-bottom: 0;
	text-align: left;
}
.ui-controlgroup-vertical .ui-controlgroup-item {
	box-sizing: border-box;
}
.ui-controlgroup .ui-controlgroup-label {
	padding: .4em 1em;
}
.ui-controlgroup .ui-controlgroup-label span {
	font-size: 80%;
}
.ui-controlgroup-horizontal .ui-controlgroup-label + .ui-controlgroup-item {
	border-left: none;
}
.ui-controlgroup-vertical .ui-controlgroup-label + .ui-controlgroup-item {
	border-top: none;
}
.ui-controlgroup-horizontal .ui-controlgroup-label.ui-widget-content {
	border-right: none;
}
.ui-controlgroup-vertical .ui-controlgroup-label.ui-widget-content {
	border-bottom: none;
}

/* Spinner specific style fixes */
.ui-controlgroup-vertical .ui-spinner-input {

	/* Support: IE8 only, Android < 4.4 only */
	width: 75%;
	width: calc( 100% - 2.4em );
}
.ui-controlgroup-vertical .ui-spinner .ui-spinner-up {
	border-top-style: solid;
}

.ui-checkboxradio-label .ui-icon-background {
	box-shadow: inset 1px 1px 1px #ccc;
	border-radius: .12em;
	border: none;
}
.ui-checkboxradio-radio-label .ui-icon-background {
	width: 16px;
	height: 16px;
	border-radius: 1em;
	overflow: visible;
	border: none;
}
.ui-checkboxradio-radio-label.ui-checkboxradio-checked .ui-icon,
.ui-checkboxradio-radio-label.ui-checkboxradio-checked:hover .ui-icon {
	background-image: none;
	width: 8px;
	height: 8px;
	border-width: 4px;
	border-style: solid;
}
.ui-checkboxradio-disabled {
	pointer-events: none;
}
.ui-datepicker {
	width: 17em;
	padding: .2em .2em 0;
	display: none;
}
.ui-datepicker .ui-datepicker-header {
	position: relative;
	padding: .2em 0;
}
.ui-datepicker .ui-datepicker-prev,
.ui-datepicker .ui-datepicker-next {
	position: absolute;
	top: 2px;
	width: 1.8em;
	height: 1.8em;
}
.ui-datepicker .ui-datepicker-prev-hover,
.ui-datepicker .ui-datepicker-next-hover {
	top: 1px;
}
.ui-datepicker .ui-datepicker-prev {
	left: 2px;
}
.ui-datepicker .ui-datepicker-next {
	right: 2px;
}
.ui-datepicker .ui-datepicker-prev-hover {
	left: 1px;
}
.ui-datepicker .ui-datepicker-next-hover {
	right: 1px;
}
.ui-datepicker .ui-datepicker-prev span,
.ui-datepicker .ui-datepicker-next span {
	display: block;
	position: absolute;
	left: 50%;
	margin-left: -8px;
	top: 50%;
	margin-top: -8px;
}
.ui-datepicker .ui-datepicker-title {
	margin: 0 2.3em;
	line-height: 1.8em;
	text-align: center;
}
.ui-datepicker .ui-datepicker-title select {
	font-size: 1em;
	margin: 1px 0;
}
.ui-datepicker select.ui-datepicker-month,
.ui-datepicker select.ui-datepicker-year {
	width: 45%;
}
.ui-datepicker table {
	width: 100%;
	font-size: .9em;
	border-collapse: collapse;
	margin: 0 0 .4em;
}
.ui-datepicker th {
	padding: .7em .3em;
	text-align: center;
	font-weight: bold;
	border: 0;
}
.ui-datepicker td {
	border: 0;
	padding: 1px;
}
.ui-datepicker td span,
.ui-datepicker td a {
	display: block;
	padding: .2em;
	text-align: right;
	text-decoration: none;
}
.ui-datepicker .ui-datepicker-buttonpane {
	background-image: none;
	margin: .7em 0 0 0;
	padding: 0 .2em;
	border-left: 0;
	border-right: 0;
	border-bottom: 0;
}
.ui-datepicker .ui-datepicker-buttonpane button {
	float: right;
	margin: .5em .2em .4em;
	cursor: pointer;
	padding: .2em .6em .3em .6em;
	width: auto;
	overflow: visible;
}
.ui-datepicker .ui-datepicker-buttonpane button.ui-datepicker-current {
	float: left;
}

/* with multiple calendars */
.ui-datepicker.ui-datepicker-multi {
	width: auto;
}
.ui-datepicker-multi .ui-datepicker-group {
	float: left;
}
.ui-datepicker-multi .ui-datepicker-group table {
	width: 95%;
	margin: 0 auto .4em;
}
.ui-datepicker-multi-2 .ui-datepicker-group {
	width: 50%;
}
.ui-datepicker-multi-3 .ui-datepicker-group {
	width: 33.3%;
}
.ui-datepicker-multi-4 .ui-datepicker-group {
	width: 25%;
}
.ui-datepicker-multi .ui-datepicker-group-last .ui-datepicker-header,
.ui-datepicker-multi .ui-datepicker-group-middle .ui-datepicker-header {
	border-left-width: 0;
}
.ui-datepicker-multi .ui-datepicker-buttonpane {
	clear: left;
}
.ui-datepicker-row-break {
	clear: both;
	width: 100%;
	font-size: 0;
}

/* RTL support */
.ui-datepicker-rtl {
	direction: rtl;
}
.ui-datepicker-rtl .ui-datepicker-prev {
	right: 2px;
	left: auto;
}
.ui-datepicker-rtl .ui-datepicker-next {
	left: 2px;
	right: auto;
}
.ui-datepicker-rtl .ui-datepicker-prev:hover {
	right: 1px;
	left: auto;
}
.ui-datepicker-rtl .ui-datepicker-next:hover {
	left: 1px;
	right: auto;
}
.ui-datepicker-rtl .ui-datepicker-buttonpane {
	clear: right;
}
.ui-datepicker-rtl .ui-datepicker-buttonpane button {
	float: left;
}
.ui-datepicker-rtl .ui-datepicker-buttonpane button.ui-datepicker-current,
.ui-datepicker-rtl .ui-datepicker-group {
	float: right;
}
.ui-datepicker-rtl .ui-datepicker-group-last .ui-datepicker-header,
.ui-datepicker-rtl .ui-datepicker-group-middle .ui-datepicker-header {
	border-right-width: 0;
	border-left-width: 1px;
}

/* Icons */
.ui-datepicker .ui-icon {
	display: block;
	text-indent: -99999px;
	overflow: hidden;
	background-repeat: no-repeat;
	left: .5em;
	top: .3em;
}
.ui-dialog {
	position: absolute;
	top: 0;
	left: 0;
	padding: .2em;
	outline: 0;
}
.ui-dialog .ui-dialog-titlebar {
	padding: .4em 1em;
	position: relative;
}
.ui-dialog .ui-dialog-title {
	float: left;
	margin: .1em 0;
	white-space: nowrap;
	width: 90%;
	overflow: hidden;
	text-overflow: ellipsis;
}
.ui-dialog .ui-dialog-titlebar-close {
	position: absolute;
	right: .3em;
	top: 50%;
	width: 20px;
	margin: -10px 0 0 0;
	padding: 1px;
	height: 20px;
}
.ui-dialog .ui-dialog-content {
	position: relative;
	border: 0;
	padding: .5em 1em;
	background: none;
	overflow: auto;
}
.ui-dialog .ui-dialog-buttonpane {
	text-align: left;
	border-width: 1px 0 0 0;
	background-image: none;
	margin-top: .5em;
	padding: .3em 1em .5em .4em;
}
.ui-dialog .ui-dialog-buttonpane .ui-dialog-buttonset {
	float: right;
}
.ui-dialog .ui-dialog-buttonpane button {
	margin: .5em .4em .5em 0;
	cursor: pointer;
}
.ui-dialog .ui-resizable-n {
	height: 2px;
	top: 0;
}
.ui-dialog .ui-resizable-e {
	width: 2px;
	right: 0;
}
.ui-dialog .ui-resizable-s {
	height: 2px;
	bottom: 0;
}
.ui-dialog .ui-resizable-w {
	width: 2px;
	left: 0;
}
.ui-dialog .ui-resizable-se,
.ui-dialog .ui-resizable-sw,
.ui-dialog .ui-resizable-ne,
.ui-dialog .ui-resizable-nw {
	width: 7px;
	height: 7px;
}
.ui-dialog .ui-resizable-se {
	right: 0;
	bottom: 0;
}
.ui-dialog .ui-resizable-sw {
	left: 0;
	bottom: 0;
}
.ui-dialog .ui-resizable-ne {
	right: 0;
	top: 0;
}
.ui-dialog .ui-resizable-nw {
	left: 0;
	top: 0;
}
.ui-draggable .ui-dialog-titlebar {
	cursor: move;
}
.ui-draggable-handle {
	-ms-touch-action: none;
	touch-action: none;
}
.ui-resizable {
	position: relative;
}
.ui-resizable-handle {
	position: absolute;
	font-size: 0.1px;
	display: block;
	-ms-touch-action: none;
	touch-action: none;
}
.ui-resizable-disabled .ui-resizable-handle,
.ui-resizable-autohide .ui-resizable-handle {
	display: none;
}
.ui-resizable-n {
	cursor: n-resize;
	height: 7px;
	width: 100%;
	top: -5px;
	left: 0;
}
.ui-resizable-s {
	cursor: s-resize;
	height: 7px;
	width: 100%;
	bottom: -5px;
	left: 0;
}
.ui-resizable-e {
	cursor: e-resize;
	width: 7px;
	right: -5px;
	top: 0;
	height: 100%;
}
.ui-resizable-w {
	cursor: w-resize;
	width: 7px;
	left: -5px;
	top: 0;
	height: 100%;
}
.ui-resizable-se {
	cursor: se-resize;
	width: 12px;
	height: 12px;
	right: 1px;
	bottom: 1px;
}
.ui-resizable-sw {
	cursor: sw-resize;
	width: 9px;
	height: 9px;
	left: -5px;
	bottom: -5px;
}
.ui-resizable-nw {
	cursor: nw-resize;
	width: 9px;
	height: 9px;
	left: -5px;
	top: -5px;
}
.ui-resizable-ne {
	cursor: ne-resize;
	width: 9px;
	height: 9px;
	right: -5px;
	top: -5px;
}
.ui-progressbar {
	height: 2em;
	text-align: left;
	overflow: hidden;
}
.ui-progressbar .ui-progressbar-value {
	margin: -1px;
	height: 100%;
}
.ui-progressbar .ui-progressbar-overlay {
	background: url("data:image/gif;base64,R0lGODlhKAAoAIABAAAAAP///yH/C05FVFNDQVBFMi4wAwEAAAAh+QQJAQABACwAAAAAKAAoAAACkYwNqXrdC52DS06a7MFZI+4FHBCKoDeWKXqymPqGqxvJrXZbMx7Ttc+w9XgU2FB3lOyQRWET2IFGiU9m1frDVpxZZc6bfHwv4c1YXP6k1Vdy292Fb6UkuvFtXpvWSzA+HycXJHUXiGYIiMg2R6W459gnWGfHNdjIqDWVqemH2ekpObkpOlppWUqZiqr6edqqWQAAIfkECQEAAQAsAAAAACgAKAAAApSMgZnGfaqcg1E2uuzDmmHUBR8Qil95hiPKqWn3aqtLsS18y7G1SzNeowWBENtQd+T1JktP05nzPTdJZlR6vUxNWWjV+vUWhWNkWFwxl9VpZRedYcflIOLafaa28XdsH/ynlcc1uPVDZxQIR0K25+cICCmoqCe5mGhZOfeYSUh5yJcJyrkZWWpaR8doJ2o4NYq62lAAACH5BAkBAAEALAAAAAAoACgAAAKVDI4Yy22ZnINRNqosw0Bv7i1gyHUkFj7oSaWlu3ovC8GxNso5fluz3qLVhBVeT/Lz7ZTHyxL5dDalQWPVOsQWtRnuwXaFTj9jVVh8pma9JjZ4zYSj5ZOyma7uuolffh+IR5aW97cHuBUXKGKXlKjn+DiHWMcYJah4N0lYCMlJOXipGRr5qdgoSTrqWSq6WFl2ypoaUAAAIfkECQEAAQAsAAAAACgAKAAAApaEb6HLgd/iO7FNWtcFWe+ufODGjRfoiJ2akShbueb0wtI50zm02pbvwfWEMWBQ1zKGlLIhskiEPm9R6vRXxV4ZzWT2yHOGpWMyorblKlNp8HmHEb/lCXjcW7bmtXP8Xt229OVWR1fod2eWqNfHuMjXCPkIGNileOiImVmCOEmoSfn3yXlJWmoHGhqp6ilYuWYpmTqKUgAAIfkECQEAAQAsAAAAACgAKAAAApiEH6kb58biQ3FNWtMFWW3eNVcojuFGfqnZqSebuS06w5V80/X02pKe8zFwP6EFWOT1lDFk8rGERh1TTNOocQ61Hm4Xm2VexUHpzjymViHrFbiELsefVrn6XKfnt2Q9G/+Xdie499XHd2g4h7ioOGhXGJboGAnXSBnoBwKYyfioubZJ2Hn0RuRZaflZOil56Zp6iioKSXpUAAAh+QQJAQABACwAAAAAKAAoAAACkoQRqRvnxuI7kU1a1UU5bd5tnSeOZXhmn5lWK3qNTWvRdQxP8qvaC+/yaYQzXO7BMvaUEmJRd3TsiMAgswmNYrSgZdYrTX6tSHGZO73ezuAw2uxuQ+BbeZfMxsexY35+/Qe4J1inV0g4x3WHuMhIl2jXOKT2Q+VU5fgoSUI52VfZyfkJGkha6jmY+aaYdirq+lQAACH5BAkBAAEALAAAAAAoACgAAAKWBIKpYe0L3YNKToqswUlvznigd4wiR4KhZrKt9Upqip61i9E3vMvxRdHlbEFiEXfk9YARYxOZZD6VQ2pUunBmtRXo1Lf8hMVVcNl8JafV38aM2/Fu5V16Bn63r6xt97j09+MXSFi4BniGFae3hzbH9+hYBzkpuUh5aZmHuanZOZgIuvbGiNeomCnaxxap2upaCZsq+1kAACH5BAkBAAEALAAAAAAoACgAAAKXjI8By5zf4kOxTVrXNVlv1X0d8IGZGKLnNpYtm8Lr9cqVeuOSvfOW79D9aDHizNhDJidFZhNydEahOaDH6nomtJjp1tutKoNWkvA6JqfRVLHU/QUfau9l2x7G54d1fl995xcIGAdXqMfBNadoYrhH+Mg2KBlpVpbluCiXmMnZ2Sh4GBqJ+ckIOqqJ6LmKSllZmsoq6wpQAAAh+QQJAQABACwAAAAAKAAoAAAClYx/oLvoxuJDkU1a1YUZbJ59nSd2ZXhWqbRa2/gF8Gu2DY3iqs7yrq+xBYEkYvFSM8aSSObE+ZgRl1BHFZNr7pRCavZ5BW2142hY3AN/zWtsmf12p9XxxFl2lpLn1rseztfXZjdIWIf2s5dItwjYKBgo9yg5pHgzJXTEeGlZuenpyPmpGQoKOWkYmSpaSnqKileI2FAAACH5BAkBAAEALAAAAAAoACgAAAKVjB+gu+jG4kORTVrVhRlsnn2dJ3ZleFaptFrb+CXmO9OozeL5VfP99HvAWhpiUdcwkpBH3825AwYdU8xTqlLGhtCosArKMpvfa1mMRae9VvWZfeB2XfPkeLmm18lUcBj+p5dnN8jXZ3YIGEhYuOUn45aoCDkp16hl5IjYJvjWKcnoGQpqyPlpOhr3aElaqrq56Bq7VAAAOw==");
	height: 100%;
	filter: alpha(opacity=25); /* support: IE8 */
	opacity: 0.25;
}
.ui-progressbar-indeterminate .ui-progressbar-value {
	background-image: none;
}
.ui-selectable {
	-ms-touch-action: none;
	touch-action: none;
}
.ui-selectable-helper {
	position: absolute;
	z-index: 100;
	border: 1px dotted black;
}
.ui-selectmenu-menu {
	padding: 0;
	margin: 0;
	position: absolute;
	top: 0;
	left: 0;
	display: none;
}
.ui-selectmenu-menu .ui-menu {
	overflow: auto;
	overflow-x: hidden;
	padding-bottom: 1px;
}
.ui-selectmenu-menu .ui-menu .ui-selectmenu-optgroup {
	font-size: 1em;
	font-weight: bold;
	line-height: 1.5;
	padding: 2px 0.4em;
	margin: 0.5em 0 0 0;
	height: auto;
	border: 0;
}
.ui-selectmenu-open {
	display: block;
}
.ui-selectmenu-text {
	display: block;
	margin-right: 20px;
	overflow: hidden;
	text-overflow: ellipsis;
}
.ui-selectmenu-button.ui-button {
	text-align: left;
	white-space: nowrap;
	width: 14em;
}
.ui-selectmenu-icon.ui-icon {
	float: right;
	margin-top: 0;
}
.ui-slider {
	position: relative;
	text-align: left;
}
.ui-slider .ui-slider-handle {
	position: absolute;
	z-index: 2;
	width: 1.2em;
	height: 1.2em;
	cursor: default;
	-ms-touch-action: none;
	touch-action: none;
}
.ui-slider .ui-slider-range {
	position: absolute;
	z-index: 1;
	font-size: .7em;
	display: block;
	border: 0;
	background-position: 0 0;
}

/* support: IE8 - See #6727 */
.ui-slider.ui-state-disabled .ui-slider-handle,
.ui-slider.ui-state-disabled .ui-slider-range {
	filter: inherit;
}

.ui-slider-horizontal {
	height: .8em;
}
.ui-slider-horizontal .ui-slider-handle {
	top: -.3em;
	margin-left: -.6em;
}
.ui-slider-horizontal .ui-slider-range {
	top: 0;
	height: 100%;
}
.ui-slider-horizontal .ui-slider-range-min {
	left: 0;
}
.ui-slider-horizontal .ui-slider-range-max {
	right: 0;
}

.ui-slider-vertical {
	width: .8em;
	height: 100px;
}
.ui-slider-vertical .ui-slider-handle {
	left: -.3em;
	margin-left: 0;
	margin-bottom: -.6em;
}
.ui-slider-vertical .ui-slider-range {
	left: 0;
	width: 100%;
}
.ui-slider-vertical .ui-slider-range-min {
	bottom: 0;
}
.ui-slider-vertical .ui-slider-range-max {
	top: 0;
}
.ui-sortable-handle {
	-ms-touch-action: none;
	touch-action: none;
}
.ui-spinner {
	position: relative;
	display: inline-block;
	overflow: hidden;
	padding: 0;
	vertical-align: middle;
}
.ui-spinner-input {
	border: none;
	background: none;
	color: inherit;
	padding: .222em 0;
	margin: .2em 0;
	vertical-align: middle;
	margin-left: .4em;
	margin-right: 2em;
}
.ui-spinner-button {
	width: 1.6em;
	height: 50%;
	font-size: .5em;
	padding: 0;
	margin: 0;
	text-align: center;
	position: absolute;
	cursor: default;
	display: block;
	overflow: hidden;
	right: 0;
}
/* more specificity required here to override default borders */
.ui-spinner a.ui-spinner-button {
	border-top-style: none;
	border-bottom-style: none;
	border-right-style: none;
}
.ui-spinner-up {
	top: 0;
}
.ui-spinner-down {
	bottom: 0;
}
.ui-tabs {
	position: relative;/* position: relative prevents IE scroll bug (element with position: relative inside container with overflow: auto appear as "fixed") */
	padding: .2em;
}
.ui-tabs .ui-tabs-nav {
	margin: 0;
	padding: .2em .2em 0;
}
.ui-tabs .ui-tabs-nav li {
	list-style: none;
	float: left;
	position: relative;
	top: 0;
	margin: 1px .2em 0 0;
	border-bottom-width: 0;
	padding: 0;
	white-space: nowrap;
}
.ui-tabs .ui-tabs-nav .ui-tabs-anchor {
	float: left;
	padding: .5em 1em;
	text-decoration: none;
}
.ui-tabs .ui-tabs-nav li.ui-tabs-active {
	margin-bottom: -1px;
	padding-bottom: 1px;
}
.ui-tabs .ui-tabs-nav li.ui-tabs-active .ui-tabs-anchor,
.ui-tabs .ui-tabs-nav li.ui-state-disabled .ui-tabs-anchor,
.ui-tabs .ui-tabs-nav li.ui-tabs-loading .ui-tabs-anchor {
	cursor: text;
}
.ui-tabs-collapsible .ui-tabs-nav li.ui-tabs-active .ui-tabs-anchor {
	cursor: pointer;
}
.ui-tabs .ui-tabs-panel {
	display: block;
	border-width: 0;
	padding: 1em 1.4em;
	background: none;
}
.ui-tooltip {
	padding: 8px;
	position: absolute;
	z-index: 9999;
	max-width: 300px;
}
body .ui-tooltip {
	border-width: 2px;
}
/* Component containers
----------------------------------*/
.ui-widget {
	font-family: Philosopher, BoldItalic;
	font-size: 1em;
}
.ui-widget .ui-widget {
	font-size: 1em;
}
.ui-widget input,
.ui-widget select,
.ui-widget textarea,
.ui-widget button {
	font-family: Philosopher,BoldItalic;
	font-size: 1em;
}
.ui-widget.ui-widget-content {
	border: 1px solid #c5c5c5;
}
.ui-widget-content {/*color del contenido de la pesta??a*/
	border: 1px solid #dddddd;
	background: rgb(91,0,10); /* Old browsers */
background: -moz-linear-gradient(top, rgba(91,0,10,1) 0%, rgba(153,0,12,1) 3%, rgba(112,0,14,1) 13%, rgba(91,0,10,1) 18%, rgba(153,0,12,1) 24%, rgba(153,0,12,1) 38%, rgba(153,0,12,1) 46%, rgba(153,0,12,1) 46%, rgba(91,0,10,1) 54%, rgba(153,0,12,1) 63%, rgba(91,0,10,1) 75%, rgba(112,0,14,1) 87%, rgba(91,0,10,1) 93%, rgba(153,0,12,1) 94%, rgba(112,0,14,1) 100%); /* FF3.6-15 */
background: -webkit-linear-gradient(top, rgba(91,0,10,1) 0%,rgba(153,0,12,1) 3%,rgba(112,0,14,1) 13%,rgba(91,0,10,1) 18%,rgba(153,0,12,1) 24%,rgba(153,0,12,1) 38%,rgba(153,0,12,1) 46%,rgba(153,0,12,1) 46%,rgba(91,0,10,1) 54%,rgba(153,0,12,1) 63%,rgba(91,0,10,1) 75%,rgba(112,0,14,1) 87%,rgba(91,0,10,1) 93%,rgba(153,0,12,1) 94%,rgba(112,0,14,1) 100%); /* Chrome10-25,Safari5.1-6 */
background: linear-gradient(to bottom, rgba(91,0,10,1) 0%,rgba(153,0,12,1) 3%,rgba(112,0,14,1) 13%,rgba(91,0,10,1) 18%,rgba(153,0,12,1) 24%,rgba(153,0,12,1) 38%,rgba(153,0,12,1) 46%,rgba(153,0,12,1) 46%,rgba(91,0,10,1) 54%,rgba(153,0,12,1) 63%,rgba(91,0,10,1) 75%,rgba(112,0,14,1) 87%,rgba(91,0,10,1) 93%,rgba(153,0,12,1) 94%,rgba(112,0,14,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#5b000a', endColorstr='#70000e',GradientType=0 ); /* IE6-9 */
	color: #111;font-family:Philosopher-BoldItalic;
}
.ui-widget-content a {
	color: #333333;
}
.ui-widget-header {/*color contenedor de pesta??as*/
	border: 1px solid #dddddd;
	background: #000000; /* Old browsers */
	background: -moz-radial-gradient(center, ellipse cover, #000000 6%, #111111 8%, #111111 8%, #111111 14%, #111111 30%, #000000 30%, #000000 42%, #111111 42%, #111111 56%, #000000 56%, #000000 69%, #111111 69%, #111111 80%, #111111 80%, #000000 80%, #000000 80%, #000000 86%, #111111 86%); /* FF3.6-15 */
	background: -webkit-radial-gradient(center, ellipse cover, #000000 6%,#111111 8%,#111111 8%,#111111 14%,#111111 30%,#000000 30%,#000000 42%,#111111 42%,#111111 56%,#000000 56%,#000000 69%,#111111 69%,#111111 80%,#111111 80%,#000000 80%,#000000 80%,#000000 86%,#111111 86%); /* Chrome10-25,Safari5.1-6 */
	background: radial-gradient(ellipse at center, #000000 6%,#111111 8%,#111111 8%,#111111 14%,#111111 30%,#000000 30%,#000000 42%,#111111 42%,#111111 56%,#000000 56%,#000000 69%,#111111 69%,#111111 80%,#111111 80%,#000000 80%,#000000 80%,#000000 86%,#111111 86%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#000000', endColorstr='#111111',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
	color: #333333;
	font-weight: bold;
}
.ui-widget-header a {
	color: #333333;
}

/* Interaction states
----------------------------------*/
.ui-state-default,
.ui-widget-content .ui-state-default,
.ui-widget-header .ui-state-default,
.ui-button,

/* We use html here because we need a greater specificity to make sure disabled
works properly when clicked or hovered */
html .ui-button.ui-state-disabled:hover,
html .ui-button.ui-state-disabled:active {/*color de las pesta??as desactivadas*/
	border: 1px solid #c5c5c5;
	background: #000111; /* Old browsers */
	background: -moz-linear-gradient(top, #000111 1%, #1c1c1c 15%, #000111 33%, #494949 53%, #000111 72%, #232323 87%, #000111 100%); /* FF3.6-15 */
	background: -webkit-linear-gradient(top, #000111 1%,#1c1c1c 15%,#000111 33%,#494949 53%,#000111 72%,#232323 87%,#000111 100%); /* Chrome10-25,Safari5.1-6 */
	background: linear-gradient(to bottom, #000111 1%,#1c1c1c 15%,#000111 33%,#494949 53%,#000111 72%,#232323 87%,#000111 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#000111', endColorstr='#000111',GradientType=0 ); /* IE6-9 */
	font-weight: normal;
	color: #454545;
}
.ui-state-default a,
.ui-state-default a:link,
.ui-state-default a:visited,
a.ui-button,
a:link.ui-button,
a:visited.ui-button,
.ui-button {/*Color de la fuente, pesta??a desactivada*/
	color: #5C0001;
	text-decoration: none;
}
.ui-state-hover,
.ui-widget-content .ui-state-hover,
.ui-widget-header .ui-state-hover,
.ui-state-focus,
.ui-widget-content .ui-state-focus,
.ui-widget-header .ui-state-focus,
.ui-button:hover,
.ui-button:focus {/*-Pesta??a con el puntero encima*/
	border: 1px solid #cccccc;
	background: #ededed; /* Old browsers */
	background: -moz-linear-gradient(top, #ededed 1%, #ffffff 15%, #ededed 16%, #ffffff 31%, #ededed 31%, #ffffff 58%, #ededed 78%, #ffffff 78%, #ededed 78%, #ededed 91%, #ededed 91%, #ffffff 92%, #ededed 100%); /* FF3.6-15 */
	background: -webkit-linear-gradient(top, #ededed 1%,#ffffff 15%,#ededed 16%,#ffffff 31%,#ededed 31%,#ffffff 58%,#ededed 78%,#ffffff 78%,#ededed 78%,#ededed 91%,#ededed 91%,#ffffff 92%,#ededed 100%); /* Chrome10-25,Safari5.1-6 */
	background: linear-gradient(to bottom, #ededed 1%,#ffffff 15%,#ededed 16%,#ffffff 31%,#ededed 31%,#ffffff 58%,#ededed 78%,#ffffff 78%,#ededed 78%,#ededed 91%,#ededed 91%,#ffffff 92%,#ededed 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#ededed', endColorstr='#ededed',GradientType=0 ); /* IE6-9 */
	font-weight: normal;
	color: #2b2b2b;
}
.ui-state-hover a,
.ui-state-hover a:hover,
.ui-state-hover a:link,
.ui-state-hover a:visited,
.ui-state-focus a,
.ui-state-focus a:hover,
.ui-state-focus a:link,
.ui-state-focus a:visited,
a.ui-button:hover,
a.ui-button:focus {/*-Color de fuente de pesta??a desactivada*/
	color: #2C0000;
	text-decoration: none;
}

.ui-visual-focus {
	box-shadow: 0 0 3px 1px rgb(94, 158, 214);
}
.ui-state-active,
.ui-widget-content .ui-state-active,
.ui-widget-header .ui-state-active,
a.ui-button:active,
.ui-button:active,
.ui-button.ui-state-active:hover {
	border: 1px solid #000000;/**/
	/*Color pesta??a seleccionada*/
	background: rgb(91,0,10); /* Old browsers */
background: -moz-radial-gradient(center, ellipse cover, rgba(91,0,10,1) 0%, rgba(153,0,12,1) 3%, rgba(112,0,14,1) 13%, rgba(91,0,10,1) 18%, rgba(153,0,12,1) 24%, rgba(153,0,12,1) 38%, rgba(153,0,12,1) 46%, rgba(153,0,12,1) 46%, rgba(91,0,10,1) 54%, rgba(153,0,12,1) 63%, rgba(91,0,10,1) 75%, rgba(112,0,14,1) 87%, rgba(91,0,10,1) 93%, rgba(153,0,12,1) 94%, rgba(112,0,14,1) 100%); /* FF3.6-15 */
background: -webkit-radial-gradient(center, ellipse cover, rgba(91,0,10,1) 0%,rgba(153,0,12,1) 3%,rgba(112,0,14,1) 13%,rgba(91,0,10,1) 18%,rgba(153,0,12,1) 24%,rgba(153,0,12,1) 38%,rgba(153,0,12,1) 46%,rgba(153,0,12,1) 46%,rgba(91,0,10,1) 54%,rgba(153,0,12,1) 63%,rgba(91,0,10,1) 75%,rgba(112,0,14,1) 87%,rgba(91,0,10,1) 93%,rgba(153,0,12,1) 94%,rgba(112,0,14,1) 100%); /* Chrome10-25,Safari5.1-6 */
background: radial-gradient(ellipse at center, rgba(91,0,10,1) 0%,rgba(153,0,12,1) 3%,rgba(112,0,14,1) 13%,rgba(91,0,10,1) 18%,rgba(153,0,12,1) 24%,rgba(153,0,12,1) 38%,rgba(153,0,12,1) 46%,rgba(153,0,12,1) 46%,rgba(91,0,10,1) 54%,rgba(153,0,12,1) 63%,rgba(91,0,10,1) 75%,rgba(112,0,14,1) 87%,rgba(91,0,10,1) 93%,rgba(153,0,12,1) 94%,rgba(112,0,14,1) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#5b000a', endColorstr='#70000e',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
	font-weight: normal;
	color: #ffffff;
}
.ui-icon-background,
.ui-state-active .ui-icon-background {
	border: #003eff;
	background-color: #ffffff;
}
.ui-state-active a,
.ui-state-active a:link,
.ui-state-active a:visited {
	color: #ffffff;
	text-decoration: none;
}

/* Interaction Cues
----------------------------------*/
.ui-state-highlight,
.ui-widget-content .ui-state-highlight,
.ui-widget-header .ui-state-highlight {
	border: 1px solid #dad55e;
	background: #fffa90;
	color: #777620;
}
.ui-state-checked {
	border: 1px solid #dad55e;
	background: #fffa90;
}
.ui-state-highlight a,
.ui-widget-content .ui-state-highlight a,
.ui-widget-header .ui-state-highlight a {
	color: #777620;
}
.ui-state-error,
.ui-widget-content .ui-state-error,
.ui-widget-header .ui-state-error {
	border: 1px solid #f1a899;
	background: #fddfdf;
	color: #5f3f3f;
}
.ui-state-error a,
.ui-widget-content .ui-state-error a,
.ui-widget-header .ui-state-error a {
	color: #5f3f3f;
}
.ui-state-error-text,
.ui-widget-content .ui-state-error-text,
.ui-widget-header .ui-state-error-text {
	color: #5f3f3f;
}
.ui-priority-primary,
.ui-widget-content .ui-priority-primary,
.ui-widget-header .ui-priority-primary {
	font-weight: bold;
}
.ui-priority-secondary,
.ui-widget-content .ui-priority-secondary,
.ui-widget-header .ui-priority-secondary {
	opacity: .7;
	filter:Alpha(Opacity=70); /* support: IE8 */
	font-weight: normal;
}
.ui-state-disabled,
.ui-widget-content .ui-state-disabled,
.ui-widget-header .ui-state-disabled {
	opacity: .35;
	filter:Alpha(Opacity=35); /* support: IE8 */
	background-image: none;
}
.ui-state-disabled .ui-icon {
	filter:Alpha(Opacity=35); /* support: IE8 - See #6059 */
}

/* Icons
----------------------------------*/

/* states and images */
.ui-icon {
	width: 16px;
	height: 16px;
}
.ui-icon,
.ui-widget-content .ui-icon {
	background-image: url("images/ui-icons_444444_256x240.png");
}
.ui-widget-header .ui-icon {
	background-image: url("images/ui-icons_444444_256x240.png");
}
.ui-state-hover .ui-icon,
.ui-state-focus .ui-icon,
.ui-button:hover .ui-icon,
.ui-button:focus .ui-icon {
	background-image: url("images/ui-icons_555555_256x240.png");
}
.ui-state-active .ui-icon,
.ui-button:active .ui-icon {
	background-image: url("images/ui-icons_ffffff_256x240.png");
}
.ui-state-highlight .ui-icon,
.ui-button .ui-state-highlight.ui-icon {
	background-image: url("images/ui-icons_777620_256x240.png");
}
.ui-state-error .ui-icon,
.ui-state-error-text .ui-icon {
	background-image: url("image/ui-icons_cc0000_256x240.png");
}
.ui-button .ui-icon {
	background-image: url("images/ui-icons_777777_256x240.png");
}

/* positioning */
.ui-icon-blank { background-position: 16px 16px; }
.ui-icon-caret-1-n { background-position: 0 0; }
.ui-icon-caret-1-ne { background-position: -16px 0; }
.ui-icon-caret-1-e { background-position: -32px 0; }
.ui-icon-caret-1-se { background-position: -48px 0; }
.ui-icon-caret-1-s { background-position: -65px 0; }
.ui-icon-caret-1-sw { background-position: -80px 0; }
.ui-icon-caret-1-w { background-position: -96px 0; }
.ui-icon-caret-1-nw { background-position: -112px 0; }
.ui-icon-caret-2-n-s { background-position: -128px 0; }
.ui-icon-caret-2-e-w { background-position: -144px 0; }
.ui-icon-triangle-1-n { background-position: 0 -16px; }
.ui-icon-triangle-1-ne { background-position: -16px -16px; }
.ui-icon-triangle-1-e { background-position: -32px -16px; }
.ui-icon-triangle-1-se { background-position: -48px -16px; }
.ui-icon-triangle-1-s { background-position: -65px -16px; }
.ui-icon-triangle-1-sw { background-position: -80px -16px; }
.ui-icon-triangle-1-w { background-position: -96px -16px; }
.ui-icon-triangle-1-nw { background-position: -112px -16px; }
.ui-icon-triangle-2-n-s { background-position: -128px -16px; }
.ui-icon-triangle-2-e-w { background-position: -144px -16px; }
.ui-icon-arrow-1-n { background-position: 0 -32px; }
.ui-icon-arrow-1-ne { background-position: -16px -32px; }
.ui-icon-arrow-1-e { background-position: -32px -32px; }
.ui-icon-arrow-1-se { background-position: -48px -32px; }
.ui-icon-arrow-1-s { background-position: -65px -32px; }
.ui-icon-arrow-1-sw { background-position: -80px -32px; }
.ui-icon-arrow-1-w { background-position: -96px -32px; }
.ui-icon-arrow-1-nw { background-position: -112px -32px; }
.ui-icon-arrow-2-n-s { background-position: -128px -32px; }
.ui-icon-arrow-2-ne-sw { background-position: -144px -32px; }
.ui-icon-arrow-2-e-w { background-position: -160px -32px; }
.ui-icon-arrow-2-se-nw { background-position: -176px -32px; }
.ui-icon-arrowstop-1-n { background-position: -192px -32px; }
.ui-icon-arrowstop-1-e { background-position: -208px -32px; }
.ui-icon-arrowstop-1-s { background-position: -224px -32px; }
.ui-icon-arrowstop-1-w { background-position: -240px -32px; }
.ui-icon-arrowthick-1-n { background-position: 1px -48px; }
.ui-icon-arrowthick-1-ne { background-position: -16px -48px; }
.ui-icon-arrowthick-1-e { background-position: -32px -48px; }
.ui-icon-arrowthick-1-se { background-position: -48px -48px; }
.ui-icon-arrowthick-1-s { background-position: -64px -48px; }
.ui-icon-arrowthick-1-sw { background-position: -80px -48px; }
.ui-icon-arrowthick-1-w { background-position: -96px -48px; }
.ui-icon-arrowthick-1-nw { background-position: -112px -48px; }
.ui-icon-arrowthick-2-n-s { background-position: -128px -48px; }
.ui-icon-arrowthick-2-ne-sw { background-position: -144px -48px; }
.ui-icon-arrowthick-2-e-w { background-position: -160px -48px; }
.ui-icon-arrowthick-2-se-nw { background-position: -176px -48px; }
.ui-icon-arrowthickstop-1-n { background-position: -192px -48px; }
.ui-icon-arrowthickstop-1-e { background-position: -208px -48px; }
.ui-icon-arrowthickstop-1-s { background-position: -224px -48px; }
.ui-icon-arrowthickstop-1-w { background-position: -240px -48px; }
.ui-icon-arrowreturnthick-1-w { background-position: 0 -64px; }
.ui-icon-arrowreturnthick-1-n { background-position: -16px -64px; }
.ui-icon-arrowreturnthick-1-e { background-position: -32px -64px; }
.ui-icon-arrowreturnthick-1-s { background-position: -48px -64px; }
.ui-icon-arrowreturn-1-w { background-position: -64px -64px; }
.ui-icon-arrowreturn-1-n { background-position: -80px -64px; }
.ui-icon-arrowreturn-1-e { background-position: -96px -64px; }
.ui-icon-arrowreturn-1-s { background-position: -112px -64px; }
.ui-icon-arrowrefresh-1-w { background-position: -128px -64px; }
.ui-icon-arrowrefresh-1-n { background-position: -144px -64px; }
.ui-icon-arrowrefresh-1-e { background-position: -160px -64px; }
.ui-icon-arrowrefresh-1-s { background-position: -176px -64px; }
.ui-icon-arrow-4 { background-position: 0 -80px; }
.ui-icon-arrow-4-diag { background-position: -16px -80px; }
.ui-icon-extlink { background-position: -32px -80px; }
.ui-icon-newwin { background-position: -48px -80px; }
.ui-icon-refresh { background-position: -64px -80px; }
.ui-icon-shuffle { background-position: -80px -80px; }
.ui-icon-transfer-e-w { background-position: -96px -80px; }
.ui-icon-transferthick-e-w { background-position: -112px -80px; }
.ui-icon-folder-collapsed { background-position: 0 -96px; }
.ui-icon-folder-open { background-position: -16px -96px; }
.ui-icon-document { background-position: -32px -96px; }
.ui-icon-document-b { background-position: -48px -96px; }
.ui-icon-note { background-position: -64px -96px; }
.ui-icon-mail-closed { background-position: -80px -96px; }
.ui-icon-mail-open { background-position: -96px -96px; }
.ui-icon-suitcase { background-position: -112px -96px; }
.ui-icon-comment { background-position: -128px -96px; }
.ui-icon-person { background-position: -144px -96px; }
.ui-icon-print { background-position: -160px -96px; }
.ui-icon-trash { background-position: -176px -96px; }
.ui-icon-locked { background-position: -192px -96px; }
.ui-icon-unlocked { background-position: -208px -96px; }
.ui-icon-bookmark { background-position: -224px -96px; }
.ui-icon-tag { background-position: -240px -96px; }
.ui-icon-home { background-position: 0 -112px; }
.ui-icon-flag { background-position: -16px -112px; }
.ui-icon-calendar { background-position: -32px -112px; }
.ui-icon-cart { background-position: -48px -112px; }
.ui-icon-pencil { background-position: -64px -112px; }
.ui-icon-clock { background-position: -80px -112px; }
.ui-icon-disk { background-position: -96px -112px; }
.ui-icon-calculator { background-position: -112px -112px; }
.ui-icon-zoomin { background-position: -128px -112px; }
.ui-icon-zoomout { background-position: -144px -112px; }
.ui-icon-search { background-position: -160px -112px; }
.ui-icon-wrench { background-position: -176px -112px; }
.ui-icon-gear { background-position: -192px -112px; }
.ui-icon-heart { background-position: -208px -112px; }
.ui-icon-star { background-position: -224px -112px; }
.ui-icon-link { background-position: -240px -112px; }
.ui-icon-cancel { background-position: 0 -128px; }
.ui-icon-plus { background-position: -16px -128px; }
.ui-icon-plusthick { background-position: -32px -128px; }
.ui-icon-minus { background-position: -48px -128px; }
.ui-icon-minusthick { background-position: -64px -128px; }
.ui-icon-close { background-position: -80px -128px; }
.ui-icon-closethick { background-position: -96px -128px; }
.ui-icon-key { background-position: -112px -128px; }
.ui-icon-lightbulb { background-position: -128px -128px; }
.ui-icon-scissors { background-position: -144px -128px; }
.ui-icon-clipboard { background-position: -160px -128px; }
.ui-icon-copy { background-position: -176px -128px; }
.ui-icon-contact { background-position: -192px -128px; }
.ui-icon-image { background-position: -208px -128px; }
.ui-icon-video { background-position: -224px -128px; }
.ui-icon-script { background-position: -240px -128px; }
.ui-icon-alert { background-position: 0 -144px; }
.ui-icon-info { background-position: -16px -144px; }
.ui-icon-notice { background-position: -32px -144px; }
.ui-icon-help { background-position: -48px -144px; }
.ui-icon-check { background-position: -64px -144px; }
.ui-icon-bullet { background-position: -80px -144px; }
.ui-icon-radio-on { background-position: -96px -144px; }
.ui-icon-radio-off { background-position: -112px -144px; }
.ui-icon-pin-w { background-position: -128px -144px; }
.ui-icon-pin-s { background-position: -144px -144px; }
.ui-icon-play { background-position: 0 -160px; }
.ui-icon-pause { background-position: -16px -160px; }
.ui-icon-seek-next { background-position: -32px -160px; }
.ui-icon-seek-prev { background-position: -48px -160px; }
.ui-icon-seek-end { background-position: -64px -160px; }
.ui-icon-seek-start { background-position: -80px -160px; }
/* ui-icon-seek-first is deprecated, use ui-icon-seek-start instead */
.ui-icon-seek-first { background-position: -80px -160px; }
.ui-icon-stop { background-position: -96px -160px; }
.ui-icon-eject { background-position: -112px -160px; }
.ui-icon-volume-off { background-position: -128px -160px; }
.ui-icon-volume-on { background-position: -144px -160px; }
.ui-icon-power { background-position: 0 -176px; }
.ui-icon-signal-diag { background-position: -16px -176px; }
.ui-icon-signal { background-position: -32px -176px; }
.ui-icon-battery-0 { background-position: -48px -176px; }
.ui-icon-battery-1 { background-position: -64px -176px; }
.ui-icon-battery-2 { background-position: -80px -176px; }
.ui-icon-battery-3 { background-position: -96px -176px; }
.ui-icon-circle-plus { background-position: 0 -192px; }
.ui-icon-circle-minus { background-position: -16px -192px; }
.ui-icon-circle-close { background-position: -32px -192px; }
.ui-icon-circle-triangle-e { background-position: -48px -192px; }
.ui-icon-circle-triangle-s { background-position: -64px -192px; }
.ui-icon-circle-triangle-w { background-position: -80px -192px; }
.ui-icon-circle-triangle-n { background-position: -96px -192px; }
.ui-icon-circle-arrow-e { background-position: -112px -192px; }
.ui-icon-circle-arrow-s { background-position: -128px -192px; }
.ui-icon-circle-arrow-w { background-position: -144px -192px; }
.ui-icon-circle-arrow-n { background-position: -160px -192px; }
.ui-icon-circle-zoomin { background-position: -176px -192px; }
.ui-icon-circle-zoomout { background-position: -192px -192px; }
.ui-icon-circle-check { background-position: -208px -192px; }
.ui-icon-circlesmall-plus { background-position: 0 -208px; }
.ui-icon-circlesmall-minus { background-position: -16px -208px; }
.ui-icon-circlesmall-close { background-position: -32px -208px; }
.ui-icon-squaresmall-plus { background-position: -48px -208px; }
.ui-icon-squaresmall-minus { background-position: -64px -208px; }
.ui-icon-squaresmall-close { background-position: -80px -208px; }
.ui-icon-grip-dotted-vertical { background-position: 0 -224px; }
.ui-icon-grip-dotted-horizontal { background-position: -16px -224px; }
.ui-icon-grip-solid-vertical { background-position: -32px -224px; }
.ui-icon-grip-solid-horizontal { background-position: -48px -224px; }
.ui-icon-gripsmall-diagonal-se { background-position: -64px -224px; }
.ui-icon-grip-diagonal-se { background-position: -80px -224px; }


/* Misc visuals
----------------------------------*/

/* Corner radius */
.ui-corner-all,
.ui-corner-top,
.ui-corner-left,
.ui-corner-tl {
	border-top-left-radius: 3px;
}
.ui-corner-all,
.ui-corner-top,
.ui-corner-right,
.ui-corner-tr {
	border-top-right-radius: 3px;
}
.ui-corner-all,
.ui-corner-bottom,
.ui-corner-left,
.ui-corner-bl {
	border-bottom-left-radius: 3px;
}
.ui-corner-all,
.ui-corner-bottom,
.ui-corner-right,
.ui-corner-br {
	border-bottom-right-radius: 3px;
}

/* Overlays */
.ui-widget-overlay {
	background: #aaaaaa;
	opacity: .3;
	filter: Alpha(Opacity=30); /* support: IE8 */
}
.ui-widget-shadow {
	-webkit-box-shadow: 0px 0px 5px #666666;
	box-shadow: 0px 0px 5px #666666;
}'''
    f.write(mensaje)
    f.close()