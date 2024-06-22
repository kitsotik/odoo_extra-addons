git checkout main
git status
git add .
$fecha = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
git commit -m "Actualizacion realizada el $($fecha)"
git push origin 16.0

