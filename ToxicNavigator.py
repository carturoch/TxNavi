import sublime
import sublime_plugin
from os import listdir

class TxNavCommand(sublime_plugin.TextCommand):
	def project_path(self):
		return sublime.active_window().folders()[0]

	def current_line(self):
		return self.view.substr(self.view.line(self.view.sel()[0]))

	def open_reference(self, path):
		files = listdir(path)
		first_file_path = path + "/" +files[0]
		sublime.active_window().open_file(first_file_path)
		sublime.active_window().run_command("reveal_in_side_bar")

	def run(self, edit):
		ref = self.current_line()
		base_path = self.project_path()
		abs_path = False
		if '%suitePath%' in ref:
			abs_path = ref.replace('%suitePath%', base_path + "/toxic/suite")
		elif '%libPath%' in ref:
			abs_path = ref.replace('%libPath%', base_path + "/toxic/library")
		if abs_path:
			print("Opening:", abs_path)
			self.open_reference(abs_path)
		else:
			print("No Tx link detected")
