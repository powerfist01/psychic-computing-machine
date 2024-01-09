
from fastapi import APIRouter
from app.services.reader import FileReader
import app.utils.functions as functions

home_router = APIRouter(
    prefix="/api",
)

@home_router.get("/read_file")
async def read_root():
    '''
        Read access is granted
    '''
    
    file_reader = FileReader('unclassified.xlsx')

    structured_data = file_reader.read_file_get_structured_data()

    for data in structured_data:

        category = data.get('category')    
        description = data.get('description')
        quantity = data.get('quantity')
        amount = data.get('amount')

        if(not category or not description or not quantity or not amount): continue

        functions.insert_into_details_table(category, description, quantity, amount)
    
    return structured_data

@home_router.post("/search")
async def read_root(search_query: str):
    '''
        Search access is granted
    '''

    if(not search_query): 
        return {'error': 'No search query provided'}

    results = functions.get_category_by_description(search_query)

    categories = set()

    for result in results:
        categories.add(result[0])

    return {'search_query': search_query, 'categories': list(categories)}