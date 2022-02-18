function nuevoOperadores() {
    $("#idoperador").val("");
    $("#idoperador").hide();
    $("#btn-buscar").hide();
    $("#btn-guardar").removeAttr("disabled");
    $("#btn-nuevo").attr("disabled", true);
}

function buscarOperadores() {
    var idoperador = $("#idoperador").val();
    if (idoperador != "") {
        $.ajax({
            url: "operadores/" + idoperador,
            method: 'GET',
            data: {},
            cache: false,
            dataType: 'json',
            success: function (respuesta) {
                if(respuesta.status=='404')
                {
                    mostrarAlerta('error','El operador no se encontró');
                }else{
                    var operador = respuesta;
                    $("#idoperador").attr("readonly", true);
                    $("#btn-buscar").attr("disabled", true);
                    $("#dni").val(operador.dni);
                    $("#nombre").val(operador.nombre);
                    $("#apellido").val(operador.apellido);
                    $("#fechanac").val(operador.fechanac);

                    $("#btn-guardar").removeAttr("disabled");
                    $("#btn-eliminar").removeAttr("disabled");
                    $("#btn-nuevo").attr("disabled", true);
                }

            },
            error: function () {
            mostrarAlerta('error',"Ocurrio un error inesperado");
            }
        });
    } else {
      mostrarAlerta('error',"Ingrese un codigo");
    }
}
function eliminarOperadores()
{
    $("[name='user-form']").append('<input type="hidden" name="eliminar" value="true">');
}

function salir() {
    window.location.href = "./operadores";
}
