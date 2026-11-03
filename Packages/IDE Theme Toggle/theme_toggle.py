import sublime
import sublime_plugin


class ToggleIdeThemeCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        settings = sublime.load_settings("Preferences.sublime-settings")
        is_light = settings.get("color_scheme") in (
            "Packages/ayu/ayu-light.sublime-color-scheme",
            "Packages/IDE Theme Toggle/Calm Light.sublime-color-scheme",
        )
        if is_light:
            settings.set("theme", "niceDarkTheme.sublime-theme")
            settings.set("color_scheme", "Packages/niceDarkTheme/JetBrains-Inspired.sublime-color-scheme")
            settings.set("file_icon_theme", "niceDarkTheme.sublime-file-icons")
        else:
            settings.set("theme", "Default.sublime-theme")
            settings.set("color_scheme", "Packages/IDE Theme Toggle/Calm Light.sublime-color-scheme")
            settings.set("file_icon_theme", "niceDarkTheme.sublime-file-icons")
        settings.set("themed_title_bar", False)
        sublime.save_settings("Preferences.sublime-settings")
