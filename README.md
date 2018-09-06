# celcat-ics-sync
Serveur python ics pour calendrier celcat web

## Compatibilité
Celcat calendar versions:
- 7.9.3373.0


## Inctallation
`sudo ./install.sh`

## Desinstallation
`sudo ./uninstall.sh`

## Configuration
Configuration au format json (/etc/celcat_ics_sync.conf.json)  
l'url du calendrier peut contenir différents tags:  
- `%type` sera remplacé par la valeur tags['type'] (dans la configuration)
- `%name` sera remplacé par la valeur tags['name']...
- `%date` sera remplacé par la date de la semaine / mois
- `%formation` sera remplacé par l'identifiant de la formation pour celcat.

Le nom de fichier ics peut contenir le tag `%name`  

### Tags
- `type` "month" ou "week"
- `name` le nom "friendly" du calendrier
- `formation` l'identifiant celcat du calendrier

### Plage de dates
`from` et `to` définissent la plage temporelle d'import de celcat.
Ce sont des entiers relatifs.
Si from vaut -1 ou -5, on commencera l'import respectivement 1 et 5 semaine avant le jour de l'import.  
Si to vaut 3 ou 10, on importera jusqu'à respectivement 3 et 10 semaines après le jour de l'import.
