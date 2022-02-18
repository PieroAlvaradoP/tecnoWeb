
function nuevoUsuario() {
    $("#idusuario").val("");
    $("#idusuario").hide();
    $("#btn-buscar").hide();
    $("#btn-guardar").removeAttr("disabled");
    $("#btn-nuevo").attr("disabled", true);
}

function buscarUsuario() {
    var idusuario = $("#idusuario").val();
    if (idusuario != "") {
        $.ajax({
            url: "usuario/" + idusuario,
            method: 'GET',
            data: {},
            cache: false,
            dataType: 'json',
            success: function (respuesta) {
                if(respuesta.status=='404')
                {
                    mostrarAlerta('error','El usuario no se encontró');
                }else{
                    var usuario = respuesta;
                    $("#idusuario").attr("readonly", true);
                    $("#btn-buscar").attr("disabled", true);

                    $("#nombre").val(usuario.nombre);
                    $("#clave").val(usuario.clave);
                    $("#estado").val(usuario.estado);

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
function eliminarUsuario()
{
    $("[name='user-form']").append('<input type="hidden" name="eliminar" value="true">');
}

function salir() {
    window.location.href = "./usuario";
}
