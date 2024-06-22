git checkout main
git status
git add .
$fecha = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
$mensaje = "Actualizacion realizada el $fecha"
git commit -m $mensaje
git push origin 16.0

