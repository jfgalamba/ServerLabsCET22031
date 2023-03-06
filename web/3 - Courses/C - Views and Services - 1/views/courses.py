from fastapi import APIRouter
from fastapi_chameleon import template

router = APIRouter()

@router.get('/courses')                            # type: ignore
@template()
async def courses():
    return {
        'available_courses': [
            {
                'id': 5,
                'category': 'Programação Web',
                'price': 190,
                'name': 'Desenvolvimento de Websites',
                'summary': 'Consectetur et, temporibus velit inventore porro sint dolore hic veniam sapiente, quos voluptatem aliquid, explicabo doloremque sunt!',
                'trainer_id': 1,
                'trainer_name': 'Osmar',
            },
            {
                'id': 6,
                'category': 'Marketing',
                'price': 250,
                'name': 'SEO - Optimizações Motores de Busca',
                'summary': 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
                'trainer_id': 4,
                'trainer_name': 'Bernardo',
            },
            {
                'id': 7,
                'category': 'Programação',
                'price': 250,
                'name': 'Programação de Device Drivers',
                'summary': 'Ex voluptatibus amet magnam maxime. Repellat quis eos laudantium magnam alias quisquam repellendus magni, quas nam vitae explicabo sed necessitatibus? Eaque!',
                'trainer_id': 2,
                'trainer_name': 'Alberta',
            },
            {
                'id': 8,
                'category': 'Electrónica',
                'price': 280,
                'name': 'Microsoldadura de SMD',
                'summary': ' Esse est nemo dolorum tempora numquam dolorem in optio sed quasi voluptate! Voluptatibus animi accusantium ad! Ratione et possimus repellendus vero nemo id modi.',
                'trainer_id': 6,
                'trainer_name': 'Roberta',
            },
        ],
    }
#:

@router.get('/courses/{course_id}')                            # type: ignore
@template()
async def course_details():
    return {
        'id': 8,
        'name': 'Microsoldadura de SMD',
        'description': 'Incidunt vero deserunt explicabo sequi perferendis. Sint, sed. Explicabo blanditiis, sunt nesciunt delectus aperiam amet dignissimos exercitationem consequuntur soluta modi dolores a placeat qui corrupti ducimus. Esse, suscipit illum natus distinctio, sint repellendus quod expedita eveniet facere consequatur quas optio corrupti ratione non veniam deleniti dolor? Repudiandae harum iste libero non reprehenderit hic distinctio maxime esse repellendus, tempora at cupiditate qui nulla numquam! Fugit, saepe.',
        'trainer_name': 'Roberta Alexandra',
        'price': 280,
        'available_seats': 40,
        'schedule': 'Segundas e Quintas, 17 às 20h',
    }
#: