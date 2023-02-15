##
## EPITECH PROJECT, 2022
## Gomoku
## File description:
## Makefile
##

NAME	=	pbrain-gomoku-ai

all:
	@cp main.py ${NAME}
	@chmod 775 ${NAME}

clean:
	@rm -rf __pycache__

fclean:	clean
	@${RM} -rf ${NAME}

re:	fclean all
