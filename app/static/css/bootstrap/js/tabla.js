function eliminar(emp_codigo){
    var atr="eliminarEmpleados("+emp_codigo+")"
    var input=document.getElementById("form_del");
    input.setAttribute("action",atr)
}

function eliminarAlum(alu_codigo){
    var atr="eliminarAlum("+alu_codigo+")"
    var form_delAlu=document.getElementById("form_delAlu");
    form_delAlu.setAttribute("action",atr)
}

function eliminarApo(apo_codigo){
    var atr="eliminarApo("+apo_codigo+")"
    var form_delApo=document.getElementById("form_delApo");
    form_delApo.setAttribute("action",atr)
}

function eliminarNot(not_codigo){
    var atr="eliminarNot("+not_codigo+")"
    var form_deNot=document.getElementById("form_deNot");
    form_deNot.setAttribute("action",atr)
}

function eliminarGra(gra_codigo){
    var atr="eliminarGra("+gra_codigo+")"
    var form_deGra=document.getElementById("form_deGra");
    form_deGra.setAttribute("action",atr)
}

function eliminarCur(cur_codigo){
    var atr="eliminarCur("+cur_codigo+")"
    var form_deCur=document.getElementById("form_deCur");
    form_deCur.setAttribute("action",atr)
}

function eliminarMat(mat_codigo){
    var atr="eliminarMat("+mat_codigo+")"
    var form_deMat=document.getElementById("form_deMat");
    form_deMat.setAttribute("action",atr)
}