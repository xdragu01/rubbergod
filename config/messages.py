from config.app_config import Config


class Messages:
    prefix = Config.default_prefix

    server_warning = "Tohle funguje jen na VUT FIT serveru."
    karma_get_missing = "Toaster pls, měl jsi bordel v DB. Musel jsem za tebe uklidit."
    missing_perms = "Na tohle nemáš práva, {user}"
    acl_help = "{user}, Použití:\n`!acl {{action}} {{table}} [args]`\n"\
               "action: add, edit, del nebo list\n"\
               "table: group, rule, role nebo user\n"\
               "Argumenty záleží na zvolené akci a tabulce: "\
               "pro přidání groupy musíte zadat název groupy a ID rodiče jako nepovinný argument."
    acl_add_group = "Group vytvořena."
    acl_edit_group = "Group změněna."
    acl_del_group = "Group smazána."
    acl_add_rule = "Pravidlo vytvořeno."
    acl_edit_rule = "Pravidlo změněno."
    acl_del_rule = "Pravidlo smazáno."
    acl_add_role = "Výjimka pro roli přidána."
    acl_edit_role = "Výjimka pro roli upravena."
    acl_del_role = "Výjimka pro roli smazána."
    acl_add_user = "Výjimka pro uživatele přidána."
    acl_edit_user = "Výjimka pro uživatele upravena."
    acl_del_user = "Výjimka pro uživatele smazána."
    no_such_command = "Takový příkaz neznám. <:sadcat:576171980118687754>"
    spamming = "{user} Nespamuj tolik <:sadcat:576171980118687754>"
    insufficient_rights = "{user}, na použití tohoto příkazu nemáš právo."
    helper_plus_only = "Na tohle mají práva jen Helper+. <:KKomrade:484470873001164817>"
    vote_room_only = "Tohle funguje jen v {room}."
    bot_room_redirect = "{user} <:sadcat:576171980118687754> 👉 " \
                        "<#{bot_room}>\n"
    covid_storno = "{user} <:WeirdChamp:680711174802899007>"
    uhoh_counter = "{uhohs} uh ohs od spuštění."
    uhoh_brief = "Vypíše počet uh ohs od spuštění"

    uptime_brief = "Vypíše čas spuštění a čas uplynulý od spuštění"
    uptime_message = "Up since:  `{boottime}`\nUptime:\t`{uptime}`"

    kachna_grillbot = "O Kachnu se teď stará Grillbot " \
                      "<:feelsWowMan:493152294712377354> Použij $kachna."

    karma = "{user} Karma uživatele `{target}` je: **{karma}** " \
            "(**{order}.**)\nA rozdal:\n" \
            "**{karma_pos}** pozitivní karmy " \
            "(**{karma_pos_order}.**)\n" \
            "**{karma_neg}** negativní karmy " \
            "(**{karma_neg_order}.**)"
    karma_brief = 'Vypíše stav vaší karmy (vč. rozdané a odebrané)'
    karma_stalk_brief = 'Vypíše karmu uživatele'
    karma_message_brief = 'Zobrazí karmu za zprávu'
    karma_get_brief = 'Vrátí karma hodnotu emotu'
    karma_getall_brief = 'Vypíše, které emoty mají hodnotu 1 a -1'
    karma_give_brief = 'Přidá karmu uživateli'
    karma_transfer_brief = 'Převede karmu z jednoho uživatele na druhého'
    karma_vote_brief = 'Odstartuje hlasování o hodnotě zatím neohodnoceného emotu'
    karma_revote_brief = 'Odstartuje hlasování o nové hodnotě emotu'
    karma_leaderboard_brief = 'Karma leaderboard'
    karma_bajkarboard_brief = 'Karma leaderboard reversed'
    karma_givingboard_brief = 'Leaderboard rozdávání pozitivní karmy'
    karma_ishaboard_brief = 'Leaderboard rozdávání negativní karmy'

    karma_invalid_command = "Neznámý karma příkaz."
    karma_vote_format = "Neočekávám žádný argument. " \
                        f"Správný formát: `{prefix}karma vote`"
    karma_vote_message_hack = "Hlasování o karma ohodnocení emotu"
    karma_vote_message = f"{karma_vote_message_hack} {{emote}}"
    karma_vote_info = "Hlasování skončí za **{delay}** " \
                      "minut a minimální počet hlasů je " \
                      "**{minimum}**."
    karma_vote_result = "Výsledek hlasování o emotu {emote} " \
                        "je {result}."
    karma_vote_notpassed = "Hlasovani o emotu {emote} neprošlo.\n" \
                           "Bylo třeba aspoň {minimum} hlasů."
    karma_vote_allvoted = "Už se hlasovalo o všech emotech."
    karma_revote_format = "Očekávám pouze formát " \
                          f"`{prefix}karma revote [emote]`"
    karma_emote_not_found = "Emote jsem na serveru nenašel."
    karma_get_format = "Použití:\n" \
                       f"`{prefix}karma getall`: " \
                       "vypíše všechny emoty s hodnotou.\n" \
                       f"`{prefix}karma get [emote]`: " \
                       "zobrazí hodnotu daného emotu."
    karma_get = "Hodnota {emote} je {value}."
    karma_get_emote_not_voted = "{emote} není ohodnocen."
    karma_give_format = "Toaster pls, formát je " \
                        f"`{prefix}karma give [number] [user(s)]`"
    karma_give_format_number = "Toaster pls, formát je " \
                               f"`{prefix}karma give " \
                               "[number, jakože číslo, " \
                               "ne {input}] [user(s)]` "
    karma_give_success = "Karma byla úspěšně přidaná."
    karma_give_negative_success = "Karma byla úspěšně odebraná."
    karma_message_format = f"{prefix}karma message [url]"
    member_not_found = "{user} Nikoho takového jsem nenašel."
    karma_lederboard_offser_error = "{user} Špatný offset, zadej kladné číslo"
    karma_web_title = "Celý leaderboard"
    karma_web = "https://karma.grillbot.cloud/"
    karma_transfer_format = f"Správný formát je `{prefix} karma transfer [od koho] [komu]`"
    karma_transfer_complete = "Karma byla úspěšně převedena z `{from_user}` na `{to_user}`:\n" \
                              "Množství karmy: **{karma}**\n" \
                              "Množství pozitivně rozdané karmy: **{positive}** \n" \
                              "Množství negativně rozdané karmy: **{negative}**"

    role_add_denied = "{user}, na přidání role {role} nemáš právo."
    role_remove_denied = "{user}, na odebrání role {role} nemáš právo."
    role_invalid_line = "{user}, řádek `{line}` je neplatný."
    role_format = "{user}, použij `!god`."
    role_not_on_server = "Nepíšeš na serveru, takže předpokládám, že myslíš role VUT FIT serveru."
    role_not_role = "{user}, {not_role} není role."
    role_invalid_emote = "{user}, {not_emote} pro roli {role} není emote."
    role_channel_copy_brief = 'Zkopíruje opravnení z jednoho kanálu na druhý'
    role_channel_clone_brief = 'Naklonuje kanál'

    random_diceroll_brief = 'Všechno možné házení kostkami'
    random_roll_brief = 'Vygeneruje náhodné celé číslo z intervalu <**first**, **second**>'
    random_flip_brief = 'Hodí mincí'
    random_pick_brief = 'Vybere jedno ze slov za otazníkem'
    random_pick_usage = '*Is foo bar? Yes No Maybe*'

    rng_generator_format = f"Použití: `{prefix}roll x [y]`\n" \
                           "rozmezí x, y jsou celá čísla,\n" \
                           "pokud y není specifikováno, " \
                           "je považováno za 0."
    rng_generator_format_number = "{user}, zadej dvě celá čísla, **integers**."

    rd_too_many_dice_in_group = "Příliš moc kostek v jedné " \
                                "skupině, maximum je {maximum}."
    rd_too_many_dice_sides = "Příliš moc stěn na kostkách, " \
                             "maximum je {maximum}."
    rd_too_many_dice_groups = "Příliš moc skupin kostek, " \
                              "maximum je {maximum}."
    rd_format = "Chybná syntaxe hodu ve skupině {group}."
    rd_help = "Formát naleznete na " \
              "https://wiki.roll20.net/Dice_Reference\n" \
              "Implementovány featury podle obsahu: **8. Drop/Keep**"

    get_code_brief = "Příkaz na získaní kódu pro verifikaci"
    verify_brief = "Verifikace studenta"
    verify_already_verified = "{user} Už jsi byl verifikován " \
                              "({admin} pls)."
    verify_send_format = "Očekávám jeden argument. " \
                         "Správný formát: " \
                         f"`{prefix}getcode FIT login, " \
                         "ve tvaru xlogin00, nebo MUNI UCO`"
    verify_send_dumbshit = "{user} Tvůj login. {emote}"
    verify_send_success = "{user} Kód byl odeslán na tvůj mail " \
                          "({mail})!\n" \
                          "Pro verifikaci použij: " \
                          f"`{prefix}verify [login] [kód]`"
    verify_send_not_found = "{user} Login nenalezen " \
                            "nebo jsi už tímhle krokem " \
                            "prošel ({admin} pls)."
    verify_verify_format = "Očekávám dva argumenty. " \
                           "Správný formát:\n" \
                           f"`{prefix}verify [FIT login nebo " \
                           "MUNI UCO] [kód]`\n" \
                           "Pro získání kódu použij\n" \
                           f"`{prefix}getcode [FIT login, ve tvaru " \
                           "xlogin00, nebo MUNI UCO]`"
    verify_verify_dumbshit = "{user} Kód, " \
                             "který ti přišel na mail. {emote}"
    verify_verify_manual = "Čauec {user}, nechám {admin}, " \
                           "aby to udělal manuálně, " \
                           "jsi shady (Year: {year})"
    verify_verify_success = "{user} Gratuluji, byl jsi verifikován!"
    verify_post_verify_info = "Podívej se do kanálů:\n" \
                              "<#591384273051975683> Pro pridani roli\n" \
                              "<#489461089432633346> Pro pravidla a další info"

    verify_verify_not_found = "{user} Login nenalezen nebo " \
                              "jsi už tímhle krokem prošel " \
                              "({admin} pls)."
    verify_verify_wrong_code = "{user} Špatný kód."

    vote_brief = "Zahájí hlasování"
    vote_format = f"Použití vote:\n`{prefix}vote [datum] [čas] [otázka]\n[emoji] " \
                                    "[odpověď 1]\n[emoji] [odpověď 2]\na tak dále`\n" \
                                    "Datum je ve formátu `dd.MM.(yy)`." \
                                    "Čas je ve formátu `hh:mm`. " \
                                    "Pouze vyplněný čas použije den odeslání zprávy, " \
                                    "pouze vyplněné datum použije čas 00:00. " \
                                    "Datum a čas jsou nepovinné argumenty, " \
                                    "hlasování bude bez jejich uvedení funkční neustále. " \
                                    "Pokud jsou vyplněny," \
                                    "bot pošle po uplynutí zprávu o výsledku," \
                                    "když ho mezitím nikdo nevypne. " \
                                    "Indikace výherné možnosti přežije i vypnutí."
    vote_not_emoji = "{not_emoji} není emoji. <:sadcat:576171980118687754>"
    vote_bad_date = "Hlasování může skončit jen v budoucnosti. <:objection:490989324125470720>"

    vote_winning = "Prozatím vyhrává možnost {winning_emoji} „{winning_option}“ s {votes} hlasy."
    vote_winning_multiple = "Prozatím vyhrávají možnosti {winning_emojis} s {votes} hlasy."

    vote_none = "Čekám na hlasy."

    vote_result = "V hlasování „{question}“ vyhrála možnost {winning_emoji} " \
                  "„{winning_option}“ s {votes} hlasy."
    vote_result_multiple = "V hlasování „{question}“ vyhrály možnosti {winning_emojis} s {votes} hlasy."
    vote_result_none = "V hlasování „{question}“ nikdo nehlasoval. <:sadcat:576171980118687754>"

    review_add_brief = 'Přidá recenzi na předmět'
    review_get_brief = 'Vypíše recenze na vybraný předmět'
    review_remove_brief = 'Odstraní hodnocení'
    subject_add_biref = 'Manuálne přidá předmět/y do reviews databáze'
    subject_remove_biref = 'Manuálne odebere předmět/y z reviews databáze'
    subject_update_biref = 'Automaticky vyhledá a přidá předměty do reviews i subject databáze'

    review_format = f"{prefix}reviews [add, remove, zkratka předmětu]"
    review_add_format = f"{prefix}reviews add {{ZkratkaPredmetu}} {{Tier (0-4, 0 je TOP)}} (VolitelnyText)\n" \
                        "Pro anonymní příspěvek použijte DM.\nNapříklad:\n`" \
                        f"{prefix}reviews add IZP 2 text recenze`"
    review_wrong_subject = "Nesprávná zkratka předmětu."
    review_tier = "Tier je z rozsahu 0-4, kde 0 je nejlepší."
    review_added = "Hodnocení předmětu bylo přidáno."
    reviews_page_e = "Zavolej reviews znovu pro aktualizaci."
    reviews_reaction_help = "Pokud byla recenze užitečná dejte 👍, jinak 👎.\n" \
                            "Pro odstranění hlasu je možné použit 🛑.\n" \
                            "Použijte reakce ◀️ a ▶️ pro navigaci mezi recenzemi.\n" \
                            "Pro navigaci v textu delších recenzí použijte 🔼 a 🔽.\n"

    review_get_format = f"{prefix}reviews [zkratka předmětu]"
    review_remove_format = f"{prefix}reviews remove [zkratka předmětu]"
    review_remove_format_admin = f"{prefix}reviews remove [zkratka předmětu, id + číslo]"
    review_remove_id_format = "reviews remove id [id]"
    review_remove_success = "Hodnocení předmětu bylo odebráno."
    review_remove_error = "Hodnocení předmětu nebylo nalezeno."
    review_add_denied = "{user}, na přidání hodnocení předmětu nemáš právo."
    review_not_on_server = "{user}, na použití tohto příkazu musíš být na FITwide serveru."
    review_legacy_clicked = "Toto review je zastaralé a již není podporováno"
    subject_format = f"{prefix}subject [add, remove, update] [zkratka předmětu]"
    subject_update_error = "Aktualizace se nezdařila."
    subject_update_success = "Předměty byly úspěšně aktualizovány."
    shorcut_brief = "Vrací stručné informace o předmětu"
    shorcut_format = f"{prefix}{{command}} [zkratka předmětu]"
    tierboard_brief = "Založeno na `reviews` z průměru tier hodnot"
    tierboard_help = "Založeno na `reviews` z průměru tier hodnot.\n"\
                     "typ -> P, V, PVT, PVA\n"\
                     "semestr -> Z, L\n"\
                     "rok -> jen pro povinné předměty e.g 1BIT, 2NADE"
    tierboard_missing_year = f"Nezadal jsi rok a nemáš školní roli\n{tierboard_help}"

    pr_meme = "https://github.com/Toaster192/rubbergod/pulls"
    uhoh = "uh oh"
    question = ["<:what:638277508541710337>",
                "<:wuuut:484470874003472394>",
                "nech mě <:sadcat:576171980118687754>"]

    name_day_cz = "Dnes má svátek {name}"
    name_day_cz_brief = "Vypíše, kdo má dnes svátek"
    name_day_sk = "Dnes má meniny {name}"
    name_day_sk_brief = "Vypíše, kto má dnes meniny"

    repost_title = "Nápověda"
    repost_description = "{user}, shoda **{value}**!"
    repost_content = "Pokud je obrázek repost, dej mu ♻️.\nJestli není, klikni tady na ❎ "\
                     "a při {limit} takových reakcích se toho upozornění smaže."

    absolvent_wrong_diploma_format = "Chybný formát čísla diplomu! Př: 123456/2019"
    absolvent_wrong_name = "Nepovedla se ověřit shoda zadaného jména s tvým předchozím záznamem o studiu na FIT VUT."
    absolvent_thesis_not_found_error = "Práce dle zadaného ID nebyla na webu nalezena."
    absolvent_web_error = "Nepovedlo se ověřit obhájení kvalifikační práce pod uvedeným číslem na webu, jménem, typem práce a rokem obhájení (dle čísla diplomu)."
    absolvent_diploma_error = "Diplom (číslo a jméno) se nepovedlo na webu ověřit."
    absolvent_success = "Diplom byl úspěšne ověřen."
    absolvent_brief = "Příkaz pro ověření absolvování studia na FIT VUT"
    absolvent_help = f"{absolvent_brief} - zadejte CASE-SENSITIVE údaje ve formátu:\n" \
        f"{prefix}{{command}} <Titul.> <Jméno> <Příjmení> <Číslo diplomu> <ID kvalifikační práce z URL na webu VUT <https://www.vutbr.cz/studenti/zav-prace> >\n" \
        "např: Bc. Josef Novák 123456/2019 135791\n" \
        "(při <https://www.vutbr.cz/studenti/zav-prace/detail/135791> nebo <https://www.vutbr.cz/studenti/zav-prace?zp_id=135791>)\n" \
        "Údaje slouží k jednorázovému ověření a nejsou nikam ukládány."

    urban_brief = "Vyhledávaní výrazu v urban slovníku"
    urban_help = f"`{prefix}urban výraz`\nPříklad:\n`{prefix}urban sure`"
    urban_not_found = "Pro daný výraz neexistuje záznam <:sadcat:576171980118687754>"

    autopin_max_pins_error = "Byl dosažen maximální počet připnutých správ."
    autopin_add_brief = "Začne sledovat zprávu jako prioritní pin.\n"
    autopin_add_unknown_message = "Očekáváno URL zprávy"
    autopin_add_done = "Priorita pinu nastavena."
    autopin_remove_brief = "Odebere sledování prioritního pinu."
    autopin_remove_not_exists = "V kanálu {channel_name} není nastavena prioritní zpráva pro piny."
    autopin_remove_done = "Priorita pinu odebrána."
    autopin_no_messages = "Ještě neexistuje žádné mapování."
    autopin_list_brief = "Zobrazí všechny piny s nastevenou prioritou"
    autopin_list_unknown_channel = "> Neznámý kanál ({channel_id})"
    autopin_list_unknown_message = "> {channel} - Neznámá zpráva"
    autopin_list_item = "> {channel} - {url}"

    on_ready_message = "<:peepowave:693070888546861096>"

    git_pull_brief = 'Stáhne aktuálni změny z repa'

    cogs_brief = 'Vypíše seznam načtených cogs'
    cog_load_brief = 'Načte cog'
    cog_unload_brief = 'Odebere cog'
    cog_reload_brief = 'Znovu načte cog'
    cog_is_loaded = 'Toto rozšíření `{cog}` je již načtené.'
    cog_unloaded = 'Rozšíření `{cog}` odebráno.'
    cog_loaded = 'Rozšíření `{cog}` načteno.'
    cog_is_unloaded = 'Toto rozšíření `{cog}` není načteno'
    cog_cannot_be_unloadable = 'Toto rozšíření `{cog}` je neodebratelné.'
    cog_reloaded = 'Rozšíření `{cog}` bylo načteno znovu.'

    config_backup_brief = "Vytvoří záložní kopii konfigurace v novém souboru"
    config_get_brief = "Získa hodnotu z konfigurace"
    config_set_brief = "Nastaví hodnotu v konfiguraci"
    config_append_brief = "Přidá hodnotu do pole v konfiguraci"
    config_load_brief = "Znovu načíta třídu zo souboru. Pro aplikováni změn je potřeba znovu načíst i cog"
    config_list_brief = "Vypíše klíče konfigurace"
    config_updated = 'Config updated'
    config_loaded = 'Config loaded'
    config_wrong_key = 'Nesprávny klíč'
    config_wrong_type = 'Nesprávny typ'
    config_backup_created = 'Config backup created'
    config_append_format = f'{prefix}config append [key] hodnota/y'
    config_list_invalid_regex = 'Chybný regex\n`{regex_err}`'

    channel_help = f"{prefix}channel [clone, copy]"
    channel_copy_help = f"{prefix}channel copy [source] [destination]"
    channel_copy_done = "Práva byla skopírována."
    channel_clone_help = f"{prefix}channel clone [source] [jméno]"
    channel_clone_done = "Kanál <#{id}> byl vytvořen."

    warden_scan_brief = "Prohledá obrázky v aktuálním kanále a uloží je jako hash pro detekci repostu.\nlimit: [all | <int>]"

    weather_brief = "Vypíše informace o počasí ve zvoleném městě"

    week_brief = "Vypíše, kolikátý je zrovna týden a jestli je sudý nebo lichý"
