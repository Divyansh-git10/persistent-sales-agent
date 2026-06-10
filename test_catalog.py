from app.tools.catalog_tool import CatalogTool

tool = CatalogTool()

results = tool.search_catalog(
    "Which plan includes SSO?"
)

for result in results:
    print(result)