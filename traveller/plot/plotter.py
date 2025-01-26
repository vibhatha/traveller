import plotly.express as px


class TrendPlotter:
    def plot_trend(self, trend_data, x_col, y_col, title, xlabel, ylabel, year_col):
        fig = px.line(
            trend_data,
            x=x_col,
            y=y_col,
            color="Country",
            title=title,
            labels={x_col: xlabel, y_col: ylabel},
            facet_col=year_col,
            facet_col_wrap=1,
        )  # Facet by year

        # Auto-scale y-axis
        fig.update_yaxes(autorange=True, tickformat=".0f")

        # Customize legend to be on the right and scrollable
        fig.update_layout(
            legend=dict(
                yanchor="top",
                y=1,
                xanchor="left",
                x=1.02,
                traceorder="normal",
                title_text="Country",
                itemsizing="constant",
                itemclick="toggleothers",
                itemdoubleclick="toggle",
                font=dict(size=10),
                bordercolor="Black",
                borderwidth=1,
            ),
            margin=dict(r=200),  # Adjust right margin to accommodate the legend
        )

        fig.show()
