function nuevoMateriales() {
    $("#idmateriales").val("");
    $("#idmateriales").hide();
    $("#btn-buscar").hide();
    $("#btn-guardar").removeAttr("disabled");
    $("#btn-nuevo").attr("disabled", true);
}

function buscarMateriales() {
    var idmateriales = $("#idmateriales").val();
    if (idMateriales != "") {
        $.ajax({
            url: "materiales/" + idMateriales,
            method: 'GET',
            data: {},
            cache: false,
            dataType: 'json',
            success: function (respuesta) {
                if(respuesta.status=='404')
                {
                    mostrarAlerta('error','El Material no se encontró');
                }else{
                    var materiales = respuesta;
                    $("#idmateriales").attr("readonly", true);
                    $("#btn-buscar").attr("disabled", true);

                    $("#descripcion").val(materiales.descripcion);
                    $("#precio").val(materiales.precio);
                    $("#cantidad").val(materiales.cantidad);

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
function eliminarMateriales()
{
    $("[name='user-form']").append('<input type="hidden" name="eliminar" value="true">');
}

function salir() {
    window.location.href = "./materiales";
}