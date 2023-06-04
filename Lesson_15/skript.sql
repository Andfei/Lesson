SELECT u.username, max(f.follower_id) as max_follower FROM users u join followers f ON u.id = f.user_id GROUP BY u.username HAVING max_follower=3;
SELECT u.username, min(f.follower_id) as min_follower FROM users u join followers f ON u.id != f.follower_id GROUP BY u.username HAVING min_follower=1;
SELECT * FROM users u JOIN user_profil p on u.id = p.from_profil join profil pr on u.id = pr.id;
SELECT * FROM users u JOIN user_messages um ON u.id = um.from_user JOIN messages m ON um.message_id = m.id WHERE u.id=1 and um.to_user=3 or u.id=2;
SELECT u.username, count(*) FROM users u JOIN user_messages um on u.id=um.from_user GROUP BY u.username HAVING count(*)=2;
select avg(id) from messages;
