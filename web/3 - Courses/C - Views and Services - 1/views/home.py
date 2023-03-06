from fastapi import APIRouter, Request
from starlette.requests import Request
from fastapi_chameleon import template

router = APIRouter()

@router.get('/')                            # type: ignore
@template()
async def index(response: Request):
    return {
        'num_courses': 99,
        'num_students': 2315,
        'num_trainers': 23,
        'num_events': 159,
        'popular_courses': [
            {
                'id': 1,
                'category': 'Hotelaria e Turismo',
                'price': 169,
                'name': 'Gestor Turístico',
                'summary': 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
                'trainer_id': 1,
                'trainer_name': 'Osmar',
            },
            {
                'id': 2,
                'category': 'Programação em C++',
                'price': 250,
                'name': 'Estruturas de Dados em C++',
                'summary': 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
                'trainer_id': 4,
                'trainer_name': 'Bernardo',
            },
            {
                'id': 3,
                'category': 'Natação',
                'price': 250,
                'name': 'Estilo Borboleta',
                'summary': 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
                'trainer_id': 2,
                'trainer_name': 'Alberta',
            },
        ],
        'selected_trainers': [
            {
                'id': 2,
                'name': 'Alberta Almeida',
                'expertise': 'Programação Web',
                'presentation': 'Magni qui quod omnis unde et eos fuga et exercitationem. Odio veritatis perspiciatis quaerat qui aut aut aut',
                'twitter': 'https://twitter.com/alberta_almeida',
                'facebook': 'https://facebook.com/almeidaalberta',
                'instagram': 'https://instagram.com/albermeida',
                'linkedin': 'https://linkedin.com/prof_alberta',
            },
            {
                'id': 3,
                'name': 'Augusto Avillez',
                'expertise': 'Marketing',
                'presentation': 'Repellat fugiat adipisci nemo illum nesciunt voluptas repellendus. In architecto rerum rerum temporibus',
                'twitter': 'https://twitter.com/augusto_avillez',
                'facebook': 'https://facebook.com/augustoavillez',
                'instagram': 'https://instagram.com/augillez',
                'linkedin': 'https://linkedin.com/prof_augusto',
            },
            {
                'id': 1,
                'name': 'Osmar Tello',
                'expertise': 'Gestão de Conteúdos',
                'presentation': 'Voluptas necessitatibus occaecati quia. Earum totam consequuntur qui porro et laborum toro des clara',
                'twitter': 'https://twitter.com/osmar_tello',
                'facebook': 'https://facebook.com/osmartello',
                'instagram': 'https://instagram.com/osmello',
                'linkedin': 'https://linkedin.com/prof_osmar',
            },
        ],
    }
#:

@router.get('/about')                        # type: ignore
@template()
async def about(request: Request):
    return {
        'num_courses': 99,
        'num_students': 2315,
        'num_trainers': 23,
        'num_events': 159,
        'testimonials': [
            {
                'user_id': 239,
                'user_name': 'Saul Goodman',
                'user_occupation': 'CEO & Founder',
                'text': 'Quidem odit voluptate, obcaecati, explicabo nobis corporis perspiciatis nihil doloremque eius omnis officia voluptates, facere saepe quas consequatur aliquam unde. Ab numquam reiciendis sequi.',
            },
            {
                'user_id': 1001,
                'user_name': 'Sara Wilson',
                'user_occupation': 'Designer',
                'text': 'Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.',
            },
            {
                'user_id': 704,
                'user_name': 'Jena Karlis',
                'user_occupation': 'Store Owner',
                'text': 'Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.',
            },
            {
                'user_id': 1002,
                'user_name': 'Matt Brandon',
                'user_occupation': 'Freelancer',
                'text': 'Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.',
            },
            {
                'user_id': 1589,
                'user_name': 'John Larson',
                'user_occupation': 'Entrepreneur',
                'text': 'Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.',
            },
        ]
    }
#:
