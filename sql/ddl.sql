CREATE TABLE public.sales (
	doc_id varchar NULL,
	item varchar NULL,
	category varchar NULL,
	amount int NULL,
	price numeric NULL,
	discount numeric NULL,
	CONSTRAINT sales_unique UNIQUE (doc_id,item,category,amount,price,discount)
);