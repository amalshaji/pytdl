install:
	poetry install

test:
	make install 
	poetry run pytdl amal
	poetry run pytdl https://www.youtube.com/watch?v=-hsSAdIQufM