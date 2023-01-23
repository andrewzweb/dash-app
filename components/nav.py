import dash_bootstrap_components as dbc


class Nav:

    default = [
        {"name": "Home", "path": "/"},
        {"name": "Pie", "path": "/apps/pie"},
        {"name": "Chart", "path": "/apps/chart"},
    ]

    def __init__(self, active=None):
        self.make_nav(active)

    def make_nav(self, active):
        nav = []

        for link in self.default:

            if link["name"] == active:
                nav.append(
                    dbc.NavItem(
                        dbc.NavLink(link["name"], href=link["path"], active=True)
                    )
                )
            else:
                nav.append(dbc.NavItem(dbc.NavLink(link["name"], href=link["path"])))

        self.data = dbc.Nav(nav, pills=True)

    def render(self):
        return dbc.Row(self.data, justify="between", className="mt-6 mb-12")
