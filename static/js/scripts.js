$("document").ready(function(){

    /*
  |------------------------------------------
  | Función que desabilita el copy and paste.
  |------------------------------------------
  */
   $('#txtInput1').on("cut copy paste",function(e) {
     e.preventDefault();
   });
   $('#txtInput2').on("cut copy paste",function(e) {
     e.preventDefault();
   });
  /*
  |--------------------------------------------
  | Función que desabilita el campo del código.
  |--------------------------------------------
  */
  $("document").ready(function () {
    //$("#txtCaptcha").prop('disabled', true);
    //$('#txtCaptchaDiv').addClass('disabled');
    //$("span").unbind("click");
    //$("span").attr("disabled", true);
    //$("span").css("pointer-events", "none"); // Desabilitar el puntero para selección de texto
  });

  /*
  |--------------------------------------------------------------------------
  | Función que hace desaparecer las notificaciones(alerts) de bootstrap.
  |--------------------------------------------------------------------------
  */
  $(".alert-success").fadeTo(5000, 500).fadeOut(1000, function(){
  $(".alert-success").effect( 'blind' , "slow" );
  });

});