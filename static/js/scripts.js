/**
 * @brief Función que hace desaparecer las notificaciones(alerts) de bootstrap.
 */
$("document").ready(function () {
   $(".alert-success").fadeTo(2000, 500).fadeOut(600, function(){
    $(".alert-success").effect( 'blind' , "slow" );
  });
});
