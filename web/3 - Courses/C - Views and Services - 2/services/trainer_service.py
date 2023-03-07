from typing import List

from data.models import Trainer

def trainer_count() -> int:
    return 2315
#:

def selected_trainers(count: int) -> List[Trainer]:
    return [
        Trainer(
            id = 2,
            name = 'Alberta Almeida',
            expertise = 'Programação Web',
            presentation = 'Magni qui quod omnis unde et eos fuga et exercitationem. Odio veritatis perspiciatis quaerat qui aut aut aut',
            twitter = 'https://twitter.com/alberta_almeida',
            facebook = 'https://facebook.com/almeidaalberta',
            instagram = 'https://instagram.com/albermeida',
            linkedin = 'https://linkedin.com/prof_alberta',
        ),
        Trainer(
            id = 3,
            name = 'Augusto Avillez',
            expertise = 'Marketing',
            presentation = 'Repellat fugiat adipisci nemo illum nesciunt voluptas repellendus. In architecto rerum rerum temporibus',
            twitter = 'https://twitter.com/augusto_avillez',
            facebook = 'https://facebook.com/augustoavillez',
            instagram = 'https://instagram.com/augillez',
            linkedin = 'https://linkedin.com/prof_augusto',
        ),
        Trainer(
            id = 1,
            name = 'Osmar Tello',
            expertise = 'Gestão de Conteúdos',
            presentation = 'Voluptas necessitatibus occaecati quia. Earum totam consequuntur qui porro et laborum toro des clara',
            twitter = 'https://twitter.com/osmar_tello',
            facebook = 'https://facebook.com/osmartello',
            instagram = 'https://instagram.com/osmello',
            linkedin = 'https://linkedin.com/prof_osmar',
        ),
    ][:count]
#:

