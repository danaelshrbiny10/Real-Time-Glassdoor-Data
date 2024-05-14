PGDMP     5    -                |        	   glassdoor    12.4    12.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    88954 	   glassdoor    DATABASE     �   CREATE DATABASE glassdoor WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
    DROP DATABASE glassdoor;
                postgres    false            �            1259    88957    company    TABLE     �  CREATE TABLE public.company (
    id integer NOT NULL,
    name character varying(255),
    company_link character varying(255),
    rating double precision,
    review_count integer,
    salary_count integer,
    job_count integer,
    headquarters_location character varying(255),
    logo character varying(255),
    company_size character varying(255),
    company_size_category character varying(255),
    company_description text,
    industry character varying(255)
);
    DROP TABLE public.company;
       public         heap    postgres    false            �            1259    88955    company_id_seq    SEQUENCE     �   CREATE SEQUENCE public.company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.company_id_seq;
       public          postgres    false    203                       0    0    company_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.company_id_seq OWNED BY public.company.id;
          public          postgres    false    202            
           2604    88960 
   company id    DEFAULT     h   ALTER TABLE ONLY public.company ALTER COLUMN id SET DEFAULT nextval('public.company_id_seq'::regclass);
 9   ALTER TABLE public.company ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    202    203                      0    88957    company 
   TABLE DATA           �   COPY public.company (id, name, company_link, rating, review_count, salary_count, job_count, headquarters_location, logo, company_size, company_size_category, company_description, industry) FROM stdin;
    public          postgres    false    203   {       	           0    0    company_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.company_id_seq', 1, false);
          public          postgres    false    202            �
           2606    88965    company company_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.company DROP CONSTRAINT company_pkey;
       public            postgres    false    203               �  x��W]��F}�����V�0`���%[��R���T�`����3����;vX6R��BF��{��=� ��4�n��_��+�m���`�����)����;�wR�+��e������!��-�A��^��[y�~���'-��bf[�{��y)U�-,/G���$�I���t���p替�\�R���/�8NFI4E��ν�Y��!�WM�Boy7��uB�-uɤa�e��W2u6H^3�����g+� �Ol�ʭ��f�Z�d&t�-Ɗ�-j+rͭҌ�Y���A�,���|�d������Ͽ^�ʿg>��{�����4���u
�>�m�4��\�Bh��r:�i!�H�P�~�:��}f(I�0�k��Z�R���4�(ah&v�_S��ҋd�*e�m�|%��)2rw�U�f�[�N�+Sy�
����V������8�G�m�����B�J��Y!4�@	G���LY$�e��0�����Rr� ޳�ᛕ�r�`g9/���pd_������6R��6�l���A�s�6�:Y�}��3��B�`:���@��<:H�Q�9�\�Fi�`_��D�UD�0��I[T,�j`�4�~��R3-�\vV�$ ʩC���+9��jŌH�Z�3�����-D~��6Vhv\;c^rE�m���h x�6��Z*j�6�)<> �;��+����B�@P�5C�9=hÒ�"sЏ������戆n4z��Kv/����U�"N��8��V����yxx�:���mQK�(�A4t��w#�?�#SP�%7��{�K�\�}�}��t��������h:%48hα��FS�W��cL��A�њ�� K��Y�/�x�1�*�E���y������̍I�D�mO�Ngf<�$��(	�sf"��B�nx4�x��8�zM�r�� B�CI�'�F������]4��؛xA�`7�Ԙ����섮�-$�`�4QTN1G�tO��`z.(� ��a{���j�]�r*y�F�!��u+ޱgt�0������$�����Y��N�s�U���x��I���\fَx�P�^����{~%o�9��Q<�_\ln8���
$��b�A�،��@E�h�cLU��W��L
1���fO7o4�D�L9���]��F'C/
/z��H����m�{n��iEQ8��z�.-���Ա����˝�Qc�Ae|_Sr2~p���o
3~[n{�Qq�ta[Dݦ����A2�r�<ì�u�^��9Hfi�jK��[TF��o�%0r�ּdv�gҤ�)��s�L#��w2V.-xS� ��x�s�v�~����-��7펲��#��V1-�6�͍��xEE�J��#; �}�̇:�.)o0 �$/Mg#�/TL��k��y)����$0;
0�%F����T+p�-��&�j��x��w�
Bt�jg[v;��4���1{:�3��:��a���Q?�j>Ba�J�UV/{���E�ݤ�=^�Ģ��JGw0T�Q�=�-�Y�������gA*�`�;J��ٟ��Sp������]�x�5�ԋ������GM�f����'���������|�i��jb��b&I2�޵��<-�d<�����v ���֩N�[%�.�#��?�(A4�nD����:�A�)$��/
_���4B�[�3��P8_�� Ƥ݁     