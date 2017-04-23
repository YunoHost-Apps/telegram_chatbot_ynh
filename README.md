# Telegram chatbot for YunoHost

[![Latest Version](https://img.shields.io/badge/version-_--_-green.svg?style=flat)](https://github.com/YunoHost-Apps/telegram_chatbot_ynh/releases)
[![Status](https://img.shields.io/badge/status-testing-yellow.svg?style=flat)](https://github.com/YunoHost-Apps/telegram_chatbot_ynh/milestones)
[![Dependencies](https://img.shields.io/badge/dependencies-includes-lightgrey.svg?style=flat)](https://github.com/YunoHost-Apps/telegram_chatbot_ynh#dependencies)
[![GitHub license](https://img.shields.io/badge/license-GPLv3-blue.svg?style=flat)](https://raw.githubusercontent.com/YunoHost-Apps/telegram_chatbot_ynh/master/LICENSE)
[![Yunohost version](https://img.shields.io/badge/yunohost-2.4.2_tested-orange.svg?style=flat)](https://github.com/YunoHost/yunohost)
[![GitHub issues](https://img.shields.io/github/issues/YunoHost-Apps/telegram_chatbot_ynh.svg?style=flat)](https://github.com/YunoHost-Apps/telegram_chatbot_ynh/issues)

## Telegram chatbot c'est quoi ?

Vous permet d'installer un bot sur telegram. Vous pouvez retrouver le fichier d'exemple (chatbot.py) que vous pouvez modifier à votre guise. 

La documentation de [python telegram bot](https://pypi.python.org/pypi/python-telegram-bot)

### Créer un token pour votre bot telegram

Pour récupérer un token, il faut [créer un bot sur Telegram](https://core.telegram.org/bots#6-botfather)

### Créer un token Github

Allez sur votre profile dans github et [générer facilement un token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)

Dans cette exemple, le token pour ce bot permet de se connecter à l'API de GitHub sans avoir de limitation sur le nombre de requête.

### Installation

`$ sudo yunohost app install https://github.com/YunoHost-Apps/telegram_chatbot_ynh.git`

### Mise à jour

`$ sudo yunohost app upgrade --verbose telegram -u https://github.com/YunoHost-Apps/telegram_chatbot_ynh.git`

## Après l'installation

Pour vérifier que votre bot fonctionne bien, allez sur le bot Telegram que vous avez crée précédemment et taper **coucou**, le bot doit vous répondre. Quelques autres mots peuvent être tapés comme par exemple **Bière** ;)

Vous pouvez également recherche les applications YunoHost qui ont le plus d'étoiles en tapant **ynh mopidy libresonic** **ynh libresonic sonerezh**. Bien entendu ce bot est un peu stupid, comparer ce qui est comparable. Nous pouvons comparer Mastodon et Nextcloud **ynh mastodon nextcloud**, mais ça n'a pas beaucoup de sens car ses deux applications n'ont pas les mêmes usages.

Bref ! A vous de jouer !! ;)