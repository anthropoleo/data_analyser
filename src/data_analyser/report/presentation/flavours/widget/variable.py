from ipywidgets import widgets

from data_analyser.report.presentation.core import Variable


class WidgetVariable(Variable):
    def render(self) -> widgets.VBox:
        items = [self.content["top"].render()]
        if self.content["bottom"] is not None:
            items.append(self.content["bottom"].render())

        return widgets.VBox(items)
