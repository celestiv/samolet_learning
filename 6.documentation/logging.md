# Логирование в Django

Логирование в программировании — это как ведение дневника для вашего приложения. Оно не только помогает отследить, что происходит в программе, но и является ключевым инструментом при отладке и мониторинге. Но как понять, что, когда и зачем логировать?

- Что логировать? Всегда логируйте ошибки и исключения — это ваш первый шаг к отладке. Но не останавливайтесь на этом. Логирование успешных операций, изменений состояний и ключевых бизнес-событий также важно для понимания общей работы системы.

- Когда логировать? Логируйте события на всех уровнях вашего приложения. Это поможет вам получить полную картину происходящего. Особенно важно логировать исключения как можно ближе к месту их возникновения.

- Зачем логировать? Логирование помогает не только в отладке. Это ваш инструмент для мониторинга состояния системы и аудита. Кроме того, логи могут служить основой для автоматических оповещений о критических событиях.

## Логгер

> (logger) — это точка входа в систему протоколирования. Каждый логгер представляет собой именованное хранилище, в которое можно записывать сообщения для обработки.

Каждое сообщение, которое записывается в логгер, является записью журнала. Каждая запись журнала также имеет уровень журнала, указывающий на важность данного конкретного сообщения. Запись журнала может также содержать полезные метаданные, описывающие регистрируемое событие. Это могут быть такие детали, как трассировка стека или код ошибки.

Python определяет следующие ранги логирования, расположенные в порядке критичности:

- DEBUG — системная информация низкого уровня для отладки.
- INFO — общая информация о системе.
- WARNING — информация, содержащая предупреждение о возможной проблеме.
- ERROR — информация, описывающая возникшую серьезную проблему.
- CRITICAL — информация, описывающая возникшую критическую проблему.