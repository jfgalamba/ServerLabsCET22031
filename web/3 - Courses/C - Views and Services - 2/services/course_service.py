
from typing import List
from decimal import Decimal as dec

from data.models import Course

def course_count() -> int:
    return 199
#:

def most_popular_courses(count: int) -> List[Course]:
    return [
        Course(
            id = 1,
            category = 'Hotelaria e Turismo',
            price = dec(179),
            name = 'Gestor Turístico',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Non rem numquam debitis obcaecati unde repellendus, eaque eum est saepe accusamus molestias ipsa. Consectetur dicta fuga, fugiat veniam hic autem in cupiditate, non impedit nostrum porro! Corrupti aspernatur incidunt aliquam earum quis fugit soluta ad perspiciatis culpa eius dignissimos corporis vel optio recusandae, ipsum ullam libero id, ex harum cumque unde eveniet natus! Laboriosam voluptatem vel nemo facere non quidem officia, consequatur tenetur doloremque labore dolorum, corrupti dolore tempora ducimus!',
            trainer_id = 1,
            trainer_name = 'Osmar',
            schedule = 'Segundas e Quintas, 17 às 20h',
            available_seats = 40,
        ),
        Course(
            id = 2,
            category = 'Programação em C++',
            price = dec(250),
            name = 'Estruturas de Dados em C++',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = ' Corrupti omnis maxime voluptatem sed nobis illo dolorum corporis est laboriosam molestiae, consectetur necessitatibus nihil delectus ea ullam obcaecati magnam? Sequi quis quae voluptates rerum obcaecati modi, qui molestias sit soluta recusandae aliquid non libero voluptas ipsam dicta numquam explicabo reprehenderit animi alias totam illo autem laborum a. Corrupti nam dicta, debitis et consequatur, explicabo distinctio incidunt cumque ab ullam eum sequi? Culpa?',
            trainer_id = 4,
            trainer_name = 'Bernardo',
            schedule = 'Terças e Quartas, 17h30 às 20h30',
            available_seats = 20,
        ),
        Course(
            id = 3,
            category = 'Natação',
            price = dec(250),
            name = 'Estilo Borboleta',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut ab deserunt et vitae sunt, enim dolores beatae esse necessitatibus iusto. Error iure facere incidunt minima dolorum adipisci culpa! Maiores velit doloribus perferendis tempore, dicta est, sit necessitatibus commodi, sapiente minus quas. Vitae repellat quasi sunt, iusto atque pariatur! Suscipit sed maxime quaerat obcaecati accusamus neque nobis quidem, quisquam ducimus nemo illo corporis fugit eaque fugiat nisi, dolorum minima dignissimos, enim deserunt sint corrupti?',
            trainer_id = 2,
            trainer_name = 'Alberta',
            schedule = 'Terças e Sextas, 10 às 13h',
            available_seats = 16,
        ),
    ][:count]
#:

def available_courses(count: int = 0) -> List[Course]:
    courses = [
        Course(
            id = 5,
            category = 'Programação Web',
            price = dec(190),
            name = 'Desenvolvimento de Websites',
            summary = 'Consectetur et, temporibus velit inventore porro sint dolore hic veniam sapiente, quos voluptatem aliquid, explicabo doloremque sunt!',
            description = 'Possimus obcaecati, cumque perferendis praesentium neque est eligendi voluptatum accusantium maiores blanditiis, at minima aliquid labore alias corrupti a iusto accusamus. Et iste est eos, eligendi explicabo quae illum nesciunt quis laborum, cumque mollitia dignissimos labore nisi laudantium accusamus modi eveniet ex itaque aliquam tenetur, maiores laboriosam. Ipsam, iusto! Nesciunt, impedit reiciendis. Repudiandae harum iste libero non reprehenderit hic distinctio maxime esse repellendus, tempora at cupiditate qui nulla numquam! Fugit, saepe.',
            trainer_id = 1,
            trainer_name = 'Osmar',
            schedule = 'Segundas e Quintas, 17h às 20h',
            available_seats = 30,
        ),
        Course(
            id = 6,
            category = 'Marketing',
            price = dec(250),
            name = 'SEO - Optimizações Motores de Busca',
            summary = 'Et architecto provident deleniti facere repellat nobis iste. Id facere quia quae dolores dolorem tempore.',
            description = 'Error iure facere incidunt minima dolorum adipisci culpa! Maiores velit doloribus perferendis tempore, dicta est, sit necessitatibus commodi, sapiente minus quas. Vitae repellat quasi sunt, iusto atque pariatur! Suscipit sed maxime quaerat obcaecati accusamus neque nobis quidem, quisquam ducimus nemo illo corporis fugit eaque fugiat nisi, dolorum minima dignissimos, enim deserunt sint corrupti? Voluptas magnam molestias modi ea, sunt id nemo amet reiciendis at iusto iure nam, quas dolor tempora quo nihil voluptatem impedit harum mollitia.',
            trainer_id = 4,
            trainer_name = 'Bernardo',
            schedule = 'Terças e Quartas, 17h30 às 20h30',
            available_seats = 30,
        ),
        Course(
            id = 7,
            category = 'Programação',
            price = dec(250),
            name = 'Programação de Device Drivers',
            summary = 'Ex voluptatibus amet magnam maxime. Repellat quis eos laudantium magnam alias quisquam repellendus magni, quas nam vitae explicabo sed necessitatibus? Eaque!',
            description = 'Soluta repellendus odit est quo a at unde iure dolore, eligendi harum sint voluptas quam error atque quis laudantium eaque, beatae sunt hic commodi dicta dolor nulla corporis veritatis! Optio tenetur quae sit labore. Fugiat, sed ad voluptatem doloribus architecto, tempora, consequuntur reprehenderit explicabo dignissimos est magnam voluptate consectetur ducimus at. Vitae vero reiciendis cumque aut neque similique officiis delectus obcaecati sint odio?',
            trainer_id = 2,
            trainer_name = 'Alberta',
            schedule = 'Segundas e Sextas, 17h30 às 20h30',
            available_seats = 30,
        ),
        Course(
            id = 8,
            category = 'Electrónica',
            price = dec(280),
            name = 'Microsoldadura de SMD',
            summary = ' Esse est nemo dolorum tempora numquam dolorem in optio sed quasi voluptate! Voluptatibus animi accusantium ad! Ratione et possimus repellendus vero nemo id modi.',
            description = 'Incidunt vero deserunt explicabo sequi perferendis. Sint, sed. Explicabo blanditiis, sunt nesciunt delectus aperiam amet dignissimos exercitationem consequuntur soluta modi dolores a placeat qui corrupti ducimus. Esse, suscipit illum natus distinctio, sint repellendus quod expedita eveniet facere consequatur quas optio corrupti ratione non veniam deleniti dolor? Repudiandae harum iste libero non reprehenderit hic distinctio maxime esse repellendus, tempora at cupiditate qui nulla numquam! Fugit, saepe.',
            trainer_id = 6,
            trainer_name = 'Roberta',
            schedule = 'Segundas e Sextas, 17h30 às 20h30',
            available_seats = 30,
        ),
    ]
    return courses if count <= 0 else courses[:count]
#:

def get_course_by_id(course_id: int) -> Course | None:
    courses = available_courses(10000)
    for course in courses:
        if course.id == course_id:
            return course
    return None
#: