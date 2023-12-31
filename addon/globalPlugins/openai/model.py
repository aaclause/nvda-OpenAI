import addonHandler

addonHandler.initTranslation()

class Model:

	def __init__(
		self,
		name: str,
		description: str,
		contextWindow: int,
		maxOutputToken: int=-1,
		maxTemperature: float=2.0,
		defaultTemperature: float=1.0
	):
		self.name = name
		self.description = description
		self.contextWindow = contextWindow
		self.maxOutputToken = maxOutputToken
		self.maxTemperature = maxTemperature
		self.defaultTemperature = defaultTemperature

	def __repr__(self):
		return f"Model(name={self.name}, description={self.description}, contextWindow={self.contextWindow}, maxOutputToken={self.maxOutputToken}, maxTemperature={self.maxTemperature}, defaultTemperature={self.defaultTemperature})"

	def __str__(self):
		name = self.name
		description = self.description.rstrip('.')
		contextWindow = self.contextWindow
		maxOutputToken = self.maxOutputToken
		s = f"{name} ({description}"
		if contextWindow > 0:
			label = _("Context window:")
			s += f". {label} {contextWindow}"
		if maxOutputToken > 0:
			label = _("max output token:")
			s += f", {label} {maxOutputToken}"
		s += ')'
		return s

	def __hash__(self):
		return hash((self.name, self.contextWindow, self.maxOutputToken, self.maxTemperature, self.defaultTemperature))
