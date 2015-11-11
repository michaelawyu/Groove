CREATE	TABLE	Medium(medium_type	text,	
description	text,	
PRIMARY	KEY	(medium_type))	;

CREATE	TABLE	Genre(guid	int,	
description	text,	
name	text,
PRIMARY	KEY(guid))	;

CREATE	TABLE	Production_Company(name	text,	
description	text,	
puid	int,	
PRIMARY	KEY	(puid))	;

CREATE	TABLE	Users(name	text,	
uuid	int,	
PRIMARY	KEY	(uuid))	;

CREATE	TABLE	User_Comments	(content text,	
comment_id	int,	
stars	int,	
PRIMARY	KEY	(comment_id));

CREATE	TABLE	Post(uuid int,	
comment_id int,	
mid	int,	
time	TIMESTAMP,	
PRIMARY	KEY(uuid,	comment_id,mid),	
FOREIGN	KEY	uuid	REFERENCES	Users,	
FOREIGN	KEY	mid	REFERENCES	Music,	
FOREIGN	KEY	comment_id	REFERENCES	Comments)	;


CREATE	TABLE	STORED_ON	(medium_type	text,	
mid	int,	
PRIMARY	KEY	(mid,	medium_type)	
FOREIGN	KEY	(mid)	REFERENCES	Music,	
FOREIGN	KEY	(medium_type)	REFERENCES	Medium)	;


CREATE	TABLE	BELONGS	(guid	int,	
mid	int,	
PRIMARY	KEY	(mid,	guid)	
FOREIGN	KEY	(mid)	REFERENCES	Music,	
FOREIGN	KEY	(guid)	REFERENCES	Genre)	;



CREATE	TABLE	SUPPORT(mid	int,	
auid	int,	
roles	text,	
PRIMARY	KEY	(mid,	auid)	
FOREIGN	KEY	(mid)	REFERENCES	Music,	
FOREIGN	KEY	(auid)	REFERENCES	Artist);


CREATE	TABLE	Created_by(mid	int,	
auid	int,	
PRIMARY	KEY	(mid,auid)	
FOREIGN	KEY	(mid)	REFERENCES	Music,	
FOREIGN	KEY	(auid)	REFERENCES	Artist)	;


CREATE	TABLE	RANK(rank_number	int,	
dateandtime	TIMESTAMP,	
mid	int,	
PRIMARY	KEY	(mid,	dateandTime),	
FOREIGN	KEY	(mid)	REFERENCES	Music		
ON	DELETE	CASCADE)	;